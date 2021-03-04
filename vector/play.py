import cv2
import numpy as np
from tqdm import tqdm

from vector.config import resolution, sps, file
from vector.display import oscilloscope


def main():
    print("Reading video")

    cap = cv2.VideoCapture(file.format(".mp4"))

    frames = []

    for _ in tqdm(range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))):
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (resolution, resolution), interpolation=cv2.INTER_AREA)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        edges = cv2.flip(edges, 0)

        edges = edges / 255
        edges[(0.5 <= edges) & (edges < 1)] = 1

        frames.append(np.where(edges == 1))

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    spf = int(sps / fps)
    cap.release()

    oscilloscope(frames, fps, spf)


if __name__ == '__main__':
    main()
