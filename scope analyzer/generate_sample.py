import numpy as np

fs = 100_000          # sample rate (Hz)
duration = 0.02       # seconds
f0 = 1000             # sine frequency (Hz)
noise = 0.05

t = np.arange(0, duration, 1/fs)
v = np.sin(2*np.pi*f0*t) + noise*np.random.randn(len(t))

np.savetxt("sample_data.csv",
           np.column_stack([t, v]),
           delimiter=",",
           header="time,voltage",
           comments="")

print("Created sample_data.csv")
