import cv2
import numpy as np


def nothing(x):
    pass


def main():
    img = np.zeros((900, 900, 3), np.uint8)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.line(img, (50, 100), (800, 700), (100, 50, 20), 5)
    cv2.rectangle(img, (10, 10), (200, 200), (15, 200, 50), 5)
    cv2.circle(img, (450, 450), 100, (200, 10, 10), -1)
    cv2.putText(img, 'Hello World', (10, 600), 3, 0.5, (10, 10, 255), 1, cv2.LINE_AA)
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)

    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(1) == ord('q'):
            break
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')

        img[:] = [b, g, r]

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
