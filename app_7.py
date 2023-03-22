import cv2


def main():
    # video = cv2.VideoCapture('../sourсe_img/near.mp4')
    video = cv2.VideoCapture(0)
    cv2.namedWindow('frame')

    while True:
        flag, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, 150, 200)

        contours, h = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        cv2.drawContours(frame, [contours[0]], -1, (0, 0, 255), 2)
        cv2.imshow('frame', frame)
        cv2.imshow('edge', edge)
        if cv2.waitKey(30) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
