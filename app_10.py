import cv2

import numpy as np

kernal = np.ones((5, 5), np.uint8)


def nothing(x):
    pass


def main():
    video = cv2.VideoCapture('../sourсe_img/near.mp4')
    # video = cv2.VideoCapture(0)
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
        frame = cv2.bilateralFilter(frame, 9, 75, 75)

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
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernal)

        counters, h = cv2.findContours(closing, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        counters = sorted(counters, key=cv2.contourArea, reverse=True)

        try:
            for x in range(len(counters)):
                area = cv2.contourArea((counters[x]))
                if area > 500:
                    x, y, w, h = cv2.boundingRect(counters[x])
                    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    frame = cv2.rectangle(frame, (x, y), (x + 60, y - 25), (0, 0, 0), -1)
                    frame = cv2.circle(frame, (x + (w // 2), y + (h // 2)), 20, (0, 255, 0), 2)
                    cv2.putText(frame, "RED", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        except Exception:
            print('no')

        cv2.imshow('mask', mask)
        cv2.imshow('cl', closing)
        cv2.imshow('res', res)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
