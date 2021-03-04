import time

import numpy as np
import sounddevice as sd
from tqdm import tqdm
from scipy.io.wavfile import write

from vector.config import resolution, sps, fps, spf, file


# noinspection PyUnresolvedReferences
def oscilloscope(frames):
    duration = int(len(frames) / fps)

    x_audio = np.zeros(duration * sps)
    y_audio = np.zeros(duration * sps)

    print("Generating Waves")
    for i, frame in enumerate(tqdm(frames)):
        ii = int(i * (sps / fps))
        (x, y) = frame
        x = x / resolution
        y = y / resolution
        x = x - 0.5
        y = y - 0.5

        if int(x.shape[0] / spf) > 0:
            x = np.resize(x, spf)
            y = np.resize(y, spf)

        for j in range(x.shape[0]):
            jj = ii + j
            x_audio[jj] += x[j]
            y_audio[jj] += y[j]

    out = np.column_stack([x_audio, y_audio])

    write(file.format(".wav"), sps, out.astype(np.float32))

    sd.play(out, sps)
    time.sleep(duration)
    sd.stop()