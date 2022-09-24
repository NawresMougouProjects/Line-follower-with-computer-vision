import cv2
import numpy as np

video = cv2.VideoCapture("vid.mp4")

while True:
    ret, frame = video.read()
    if not ret:
        video = cv2.VideoCapture("vid.mp4")
        continue
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_black = np.array([0, 0, 0])
    up_black = np.array([180, 50, 100])
    mask = cv2.inRange(hsv, low_black, up_black)
    edges = cv2.Canny(mask, 75, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)



    cv2.imshow("frames", frame)
    cv2.imshow("edges", edges)
    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()