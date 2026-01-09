import numpy as np
import matplotlib.pyplot as plt

#load data from CSV file
def load_data(filename):
    """Read time and voltage from a CSV file"""
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    
    time = data[:, 0] #first column is time
    voltage = data[:, 1] #second column is voltage
    return time, voltage


#find main frequency
def find_main_frequency(time, voltage):
    """Find the strongest frequency in the voltage signal"""
    
    time_step = time[1] - time[0] #calculate samples per second
    sample_rate = 1.0 / time_step
    
   
    fft_result = np.fft.rfft(voltage)  #FFT converts time signal to frequencies
    frequencies = np.fft.rfftfreq(len(voltage), time_step)
    
    amplitudes = np.abs(fft_result) #get the strength of each frequency
    
   
    main_freq_index = np.argmax(amplitudes[1:]) + 1  #find the strongest frequency skip first cause that's DC offset
    main_frequency = frequencies[main_freq_index]
    
    return frequencies, amplitudes, main_frequency



time, voltage = load_data('sample_data.csv')

frequencies, amplitudes, main_frequency = find_main_frequency(time, voltage)

print(f"\nMain frequency found: {main_frequency:.2f} Hz")

#plot 1 would show the voltage over time
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(time, voltage)
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Signal')
plt.grid(True)

#plot 2 would show the frequency spectrum
plt.subplot(1, 2, 2)
plt.plot(frequencies, amplitudes)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Strength')
plt.title('Frequency Spectrum')
plt.xlim(0, 5000) 
plt.grid(True)

plt.tight_layout()
plt.show()






