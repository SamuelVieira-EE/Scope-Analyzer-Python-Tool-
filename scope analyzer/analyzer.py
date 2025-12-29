import argparse
import numpy as np
import matplotlib.pyplot as plt


def load_csv(path: str):
    """
    Expects a CSV with two columns: time (seconds), voltage (volts)
    Header row is OK (example: time,voltage)
    """
    data = np.genfromtxt(path, delimiter=",", skip_header=1)

    if data.ndim != 2 or data.shape[1] < 2:
        raise ValueError(
            "CSV should have at least 2 columns (time, voltage). "
            "Example header: time,voltage"
        )

    t = data[:, 0]
    v = data[:, 1]

    # Remove rows with NaNs (sometimes happen in messy exports)
    mask = np.isfinite(t) & np.isfinite(v)
    t = t[mask]
    v = v[mask]

    if len(t) < 10:
        raise ValueError("Not enough valid data rows found.")

    return t, v


def estimate_fs(t: np.ndarray) -> float:
    dt = np.diff(t)
    dt = dt[np.isfinite(dt)]
    dt = dt[dt > 0]

    if len(dt) == 0:
        raise ValueError("Could not estimate sample rate from time column.")

    fs = 1.0 / np.mean(dt)
    return fs


def amplitude_spectrum(v: np.ndarray, fs: float):
    """
    Returns freqs (Hz) and single-sided amplitude spectrum.
    Uses a Hann window to reduce spectral leakage.
    """
    v = v - np.mean(v)  # remove DC offset
    N = len(v)

    window = np.hanning(N)
    v_win = v * window

    V = np.fft.rfft(v_win)
    freqs = np.fft.rfftfreq(N, d=1.0 / fs)

    # amplitude correction (coherent gain)
    cg = np.mean(window)
    mag = np.abs(V) / (N * cg)
    if len(mag) > 2:
        mag[1:-1] *= 2.0  # single-sided spectrum (except DC & Nyquist)

    return freqs, mag


def dominant_frequency(freqs: np.ndarray, mag: np.ndarray):
    # ignore DC at index 0
    idx = np.argmax(mag[1:]) + 1
    return freqs[idx], mag[idx]


def main():
    parser = argparse.ArgumentParser(description="Simple Oscilloscope CSV Analyzer (Waveform + FFT)")
    parser.add_argument("csv_file", nargs="?", default="sample_data.csv",
                        help="Path to CSV file (default: sample_data.csv)")
    parser.add_argument("--max-hz", type=float, default=5000,
                        help="Max frequency to show on FFT plot (default: 5000 Hz)")
    args = parser.parse_args()

    t, v = load_csv(args.csv_file)
    fs = estimate_fs(t)

    freqs, mag = amplitude_spectrum(v, fs)
    f0, a0 = dominant_frequency(freqs, mag)

    print(f"File: {args.csv_file}")
    print(f"Estimated sample rate: {fs:.2f} Hz")
    print(f"Dominant frequency: {f0:.2f} Hz (amplitude ~ {a0:.4f})")

    # Waveform plot
    plt.figure()
    plt.plot(t, v)
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.title("Waveform")
    plt.grid(True)

    # FFT plot
    plt.figure()
    plt.plot(freqs, mag)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("FFT Spectrum")
    plt.grid(True)
    plt.xlim(0, min(args.max_hz, freqs[-1]))

    plt.show()


if __name__ == "__main__":
    main()
