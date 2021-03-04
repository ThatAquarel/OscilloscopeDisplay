import cv2
import numpy as np

cap = cv2.VideoCapture('badapple.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    minLineLength = 0
    maxLineGap = 0

    # lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    # for x1, y1, x2, y2 in lines[0]:
    #     cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('Frame', np.hstack((edges, )))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
