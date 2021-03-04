# Use the sounddevice module
# http://python-sounddevice.readthedocs.io/en/0.3.10/

import matplotlib.pyplot as plt
import numpy as np

# Samples per second
sps = 44100

# Frequency / pitch
freq_hz = 440.0

# Duration
duration_s = 10.0

# Attenuation so the sound is reasonable
atten = 0.3

# NumpPy magic to calculate the waveform
# target frequency / samples per second = percentage of wave (440) created by each sample
each_sample_number1 = np.arange(duration_s * sps)
waveform1 = np.sin(2 * np.pi * each_sample_number1 * freq_hz / sps)
waveform_quiet1 = waveform1 * atten

each_sample_number2 = np.arange(duration_s * sps)
waveform2 = np.cos(4 * np.pi * each_sample_number2 * freq_hz / sps)
waveform_quiet2 = waveform2 * atten

# right(x), left(y)
out = np.column_stack([waveform_quiet1, waveform_quiet2])

plt.plot(waveform_quiet1[:300])
plt.show()

plt.plot(waveform_quiet2[:300])
plt.show()

# sd.play(out, sps)
# time.sleep(duration_s)
# sd.stop()
