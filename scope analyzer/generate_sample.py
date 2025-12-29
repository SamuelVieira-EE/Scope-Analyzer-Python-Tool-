import numpy as np

# Settings for our fake signal
sample_rate = 100000        # How many measurements per second
duration = 0.02             # How long to record (seconds)
frequency = 1000            # Frequency of our sine wave (Hz)
noise_level = 0.05          # How much random noise to add

# Create time points
# Example: if duration=1 second and sample_rate=100, we get 100 time points
time_step = 1 / sample_rate
time = np.arange(0, duration, time_step)

# Create a sine wave
# Formula: sin(2 * π * frequency * time)
sine_wave = np.sin(2 * np.pi * frequency * time)

# Add some random noise to make it realistic
random_noise = noise_level * np.random.randn(len(time))
voltage = sine_wave + random_noise

# Save to CSV file
# Stack time and voltage side-by-side into columns
data = np.column_stack([time, voltage])
np.savetxt("sample_data.csv", 
           data, 
           delimiter=",", 
           header="time,voltage", 
           comments="")

print("✓ Created sample_data.csv")
print(f"  - {len(time)} data points")
print(f"  - {duration} seconds of data")
print(f"  - {frequency} Hz sine wave")
