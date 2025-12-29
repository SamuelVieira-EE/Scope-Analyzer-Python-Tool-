import numpy as np
import matplotlib.pyplot as plt

# Load the data from CSV file
def load_data(filename):
    """Read time and voltage from a CSV file"""
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    
    time = data[:, 0]      # First column is time
    voltage = data[:, 1]   # Second column is voltage
    
    return time, voltage

# Find the main frequency in the signal
def find_main_frequency(time, voltage):
    """Find the strongest frequency in the voltage signal"""
    # Calculate how many samples per second
    time_step = time[1] - time[0]
    sample_rate = 1.0 / time_step
    
    # Do the FFT (converts time signal to frequencies)
    fft_result = np.fft.rfft(voltage)
    frequencies = np.fft.rfftfreq(len(voltage), time_step)
    
    # Get the strength of each frequency
    amplitudes = np.abs(fft_result)
    
    # Find the strongest frequency (skip the first one, that's DC offset)
    main_freq_index = np.argmax(amplitudes[1:]) + 1
    main_frequency = frequencies[main_freq_index]
    
    return frequencies, amplitudes, main_frequency

print("Loading data...")
time, voltage = load_data('sample_data.csv')

print("Analyzing frequencies...")
frequencies, amplitudes, main_frequency = find_main_frequency(time, voltage)

print(f"\nMain frequency found: {main_frequency:.2f} Hz")

# Plot 1: Show the voltage over time
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(time, voltage)
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Signal')
plt.grid(True)

# Plot 2: Show the frequency spectrum
plt.subplot(1, 2, 2)
plt.plot(frequencies, amplitudes)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Strength')
plt.title('Frequency Spectrum')
plt.xlim(0, 5000)  # Only show up 5000 Hz
plt.grid(True)

plt.tight_layout()
plt.show()




