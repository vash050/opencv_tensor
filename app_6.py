import cv2


def main():
    video = cv2.VideoCapture('../sourсe_img/near.mp4')
    cv2.namedWindow('frame')

    while True:
        flag, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        framex = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        framey = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        edge = cv2.Canny(gray, 150, 220)


        cv2.imshow('framex', framex)
        cv2.imshow('framey', framey)
        cv2.imshow('edge', edge)
        if cv2.waitKey(30) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
