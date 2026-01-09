import numpy as np

#set of data or sample
sample_rate = 100000        # number of measurements per second
duration = 0.02             #length of time to record (seconds)
frequency = 1000            #frequency (Hz)
noise_level = 0.05          #noise

#create time points so if duration=1 second and sample_rate=100 there is 100 time points
time_step = 1 / sample_rate
time = np.arange(0, duration, time_step)


sine_wave = np.sin(2 * np.pi * frequency * time) #sine wave sin(2 * π * frequency * time)

# random noise to make it realistic
random_noise = noise_level * np.random.randn(len(time))
voltage = sine_wave + random_noise

# save it to a CSV file

data = np.column_stack([time, voltage]) #makes time and voltage side-by-side into columns
np.savetxt("sample_data.csv", data, delimiter=",", header="time,voltage", comments="")


print(f"  - {len(time)} data points")
print(f"  - {duration} seconds of data")
print(f"  - {frequency} Hz sine wave")

