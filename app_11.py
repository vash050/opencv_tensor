import cv2

import numpy as np


def nothing(x):
    pass


def main():
    video = cv2.VideoCapture(0)
    cv2.namedWindow('track')
    cv2.createTrackbar('T1', 'track', 0, 255, nothing)
    cv2.createTrackbar('T2', 'track', 0, 255, nothing)

    kernal = np.ones((5, 5))

    while True:
        ret, frame = video.read()
        frame = cv2.bilateralFilter(frame, 9, 75, 75)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        thresh1 = cv2.getTrackbarPos('T1', 'track')
        thresh2 = cv2.getTrackbarPos('T2', 'track')
        new_frame = cv2.Canny(gray, thresh1, thresh2)
        div = cv2.dilate(new_frame, kernal, iterations=1)

        cv2.imshow('frame', div)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
