# Scope CSV Analyzer (Waveform + FFT)

reads an oscilloscope CSV and:
- plots the waveform (time vs voltage)
- then it will plot the FFT spectrum ->(takes a signal in time from oscilloscope and converts into frequency Amplitude vs Frequency)
- Find the biggest FFT peak
- prints result

waveform -> FFT -> frequency peaks -> dominant frequency

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


