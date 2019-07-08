import cv2

fname = 'C:/Download/me.jpg'

img = cv2.imread(fname, cv2.IMREAD_COLOR)
cv2.imshow('image', img)

while True:
    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()


