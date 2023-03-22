import cv2

import numpy as np

kernal = np.ones((5, 5), np.uint8)


def nothing(x):
    pass


def main():
    video = cv2.VideoCapture('../sourсe_img/near.mp4')
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.namedWindow('cl', cv2.WINDOW_NORMAL)
    cv2.namedWindow('mask', cv2.WINDOW_NORMAL)

    cv2.createTrackbar('HL', 'frame', 0, 180, nothing)
    cv2.createTrackbar('SL', 'frame', 0, 255, nothing)
    cv2.createTrackbar('VL', 'frame', 0, 255, nothing)
    cv2.createTrackbar('H', 'frame', 0, 180, nothing)
    cv2.createTrackbar('S', 'frame', 0, 255, nothing)
    cv2.createTrackbar('V', 'frame', 0, 255, nothing)

    while True:
        ret, frame = video.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blur = cv2.GaussianBlur(frame, (5, 5), 0)

        hl = cv2.getTrackbarPos('HL', 'frame')
        sl = cv2.getTrackbarPos('SL', 'frame')
        vl = cv2.getTrackbarPos('VL', 'frame')

        h = cv2.getTrackbarPos('H', 'frame')
        s = cv2.getTrackbarPos('S', 'frame')
        v = cv2.getTrackbarPos('V', 'frame')

        lower = np.array([hl, sl, vl])
        upper = np.array([h, s, v])
        frame = cv2.bilateralFilter(frame, 9, 75, 75)
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        edge = cv2.Canny(mask, 100, 200)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernal)
        counters, h = cv2.findContours(opening, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        counters = sorted(counters, key=cv2.contourArea, reverse=True)

        try:
            cv2.drawContours(frame, [counters[0]], -1, (255, 0, 0), 5)
        except Exception:
            print('no')

        cv2.imshow('mask', mask)
        cv2.imshow('cl', closing)
        # cv2.imshow('res', res)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
