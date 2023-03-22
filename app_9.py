import cv2


def main():
    video = cv2.VideoCapture('../sourсe_img/near.mp4')

    while True:
        ret, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        flag, t1 = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
        flag, t2 = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY_INV)
        flag, t3 = cv2.threshold(frame, 127, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
        flag, t4 = cv2.threshold(frame, 127, 255, cv2.THRESH_TOZERO)
        flag, t5 = cv2.threshold(frame, 127, 255, cv2.THRESH_TOZERO_INV)

        cv2.imshow('frame', frame)
        cv2.imshow('t1', t1)
        cv2.imshow('t2', t2)
        cv2.imshow('t3', t3)
        cv2.imshow('t4', t4)
        cv2.imshow('t5', t5)

        if cv2.waitKey(30) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
