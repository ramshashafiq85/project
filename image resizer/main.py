import cv2 as cv

src = cv.imread("cute baby girl.jpg", cv.IMREAD_UNCHANGED)

cv.imshow("image", src)
scale_percent = 50
width = int(src.shape[1]*scale_percent/100)
height = int(src.shape[0]*scale_percent/100)
output = cv.resize(src, (width , height))
cv.imwrite('newimage.png' , output)
cv.waitKey(0)

