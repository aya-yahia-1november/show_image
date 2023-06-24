

import cv2
print(cv2.__version__)
img=cv2.imread("./s2.jpeg",-1)
print(img)
cv2.imshow("frist image",img)

k= cv2.waitKey(0)
if k ==27:
    cv2.destroyAllWindows()



