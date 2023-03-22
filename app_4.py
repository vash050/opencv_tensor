import cv2


def main():
    img_1 = cv2.imread('../sourсe_img/zakat-doroga-soldaty-peyzazh.jpg')
    img_2 = cv2.imread('../sourсe_img/1.jpg')

    resize_1 = cv2.resize(img_1, (900, 900))
    resize_2 = cv2.resize(img_2, (900, 900))

    frame = cv2.addWeighted(resize_1, 1,  resize_2, 0.5, 0)

    cv2.imshow('image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()