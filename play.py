import cv2
import numpy as np
from tqdm import tqdm

from display import fps, resolution, oscilloscope


def main():
    print("Reading video")
    cap = cv2.VideoCapture("./video.mp4")

    frames = []
    for _ in tqdm(range(60 * fps)):
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (resolution, resolution), interpolation=cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame, 0)
        frame = frame / 255
        frame[(0 <= frame) & (frame < 0.25)] = 0
        frame[(0.25 <= frame) & (frame < 0.6)] = 1
        frame[(0.6 <= frame) & (frame < 1)] = 2

        frames.append(frame)

    cap.release()

    frames = np.array(frames).astype(int)

    oscilloscope(frames)


if __name__ == '__main__':
    main()
