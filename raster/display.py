import time

import numpy as np
import sounddevice as sd
from scipy import signal
from scipy.io.wavfile import write
from tqdm import tqdm

from raster.config import opacity_positive, opacity_negative, file

sps = 44100
freq_hz = 90
fps = int(freq_hz / 2)
resolution = 10


def negate_frames(frames):
    print("Negating frames for better shades")
    out = np.zeros(shape=frames.shape, dtype=int)

    for i, frame in enumerate(tqdm(frames)):
        frame = frame[:-1].copy()
        empty = np.zeros(frame.shape[1], dtype=int)
        frame = np.insert(frame, 0, empty, axis=0)
        out[i] = frame

    return out


def triple_frames(frames):
    print("Tripling frames for fitting refresh rate")
    out = []

    for i in tqdm(range(frames.shape[0])):
        out.append(frames[i])
        out.append(frames[i])
        out.append(frames[i])

    return np.array(out)


# noinspection PyUnresolvedReferences
def oscilloscope(frames):
    frames = triple_frames(frames)

    duration = int(frames.shape[0] / freq_hz)

    t = np.linspace(0, duration, 44100 * duration)
    x = signal.sawtooth(2 * np.pi * freq_hz * resolution * t)

    step_x = int(sps / (resolution * freq_hz))
    step_y = int(round((step_x + 1) / 10, 0))
    steps = np.linspace(-1, 1, resolution)

    frame = 0
    n_frames = negate_frames(frames)
    y = np.zeros(x.shape)

    print("Generating Waves")
    for i in tqdm(range(resolution * duration * freq_hz)):
        frame_x = (i % (resolution * freq_hz)) % resolution

        step = steps[frame_x]
        for j in range(i * step_x, (i + 1) * step_x):
            y[j] = step

            frame_y = 0
            for k in range(0, step_x, step_y):
                if k <= (j % step_x) < (k + step_y):
                    pixel = frames[frame][frame_x][frame_y]
                    n_pixel = n_frames[frame][frame_x][frame_y]
                    y[j] += opacity_positive[pixel][j % step_x % step_y]
                    y[j] -= opacity_negative[n_pixel][j % step_x % step_y]
                frame_y += 1

        if frame_x == 9:
            frame += 1

    out = np.column_stack([y, x])

    sd.play(out, sps)
    time.sleep(duration)
    sd.stop()

    write(file.format(".wav"), sps, out.astype(np.float32))

    # plt.plot(x)
    # plt.plot(y)
    # plt.show()

    # plt.plot(x, y, '.-')
    # plt.show()


if __name__ == '__main__':
    oscilloscope(np.zeros((1 * freq_hz, resolution, resolution)).astype(int))

    # print(frames.shape)
    # frames = np.zeros((int(30 * fps), resolution, resolution), dtype=int)
    #
    # for i in range(0, int(30 * fps), fps):
    #     x = random.randint(0, 9)
    #     y = random.randint(0, 9)
    #     x1 = random.randint(0, 9)
    #     y1 = random.randint(0, 9)
    #     # x = 3
    #     # y = 3
    #     for j in range(i, i + fps):
    #         frames[j][x][y] = 2
    #         frames[j][x1][y1] = 1
