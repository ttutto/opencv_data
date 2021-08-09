import cv2

img = cv2.imread('rose.jpg')
img_crop = img[100:500, 300:700]
img_gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
img_resize = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
print(img.shape)
cv2.imshow('img', img)
cv2.imshow('crop', img_crop)
cv2.imshow('gray', img_gray)
cv2.imshow('resize', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()