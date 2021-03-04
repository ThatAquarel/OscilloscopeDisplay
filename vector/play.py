import cv2
import numpy as np
from tqdm import tqdm

from vector.config import fps, resolution, file
from vector.display import oscilloscope


def main():
    print("Reading video")

    cap = cv2.VideoCapture(file.format(".mp4"))

    frames = []

    for _ in tqdm(range(240 * fps)):
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 0)
        frame = cv2.resize(frame, (resolution, resolution), interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)

        edges = edges / 255

        edges[(0 <= edges) & (edges < 0.5)] = 0
        edges[(0.5 <= edges) & (edges < 1)] = 1

        x, y = np.where(edges == 1)
        frames.append((x, y))

    oscilloscope(frames)


if __name__ == '__main__':
    main()
