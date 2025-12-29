# Scope CSV Analyzer (Waveform + FFT)

A beginner-friendly Python project that reads an oscilloscope CSV export and:
- plots the waveform (time vs voltage)
- computes and plots the FFT spectrum
- prints the dominant frequency

## Input CSV format

CSV should have **two columns**:

time (seconds), voltage (volts)

Example:

time,voltage
0.0,0.01
0.00001,0.15
...

## Setup

```bash
pip install -r requirements.txt
