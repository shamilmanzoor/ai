import cv2
image=cv2.imread('lena.jpg',1)

cv2.line(image,(0,0),(550,550),(255,0,0),5)

cv2.rectangle(image,(75,250),(470,400),(0,255,0),4)

cv2.circle(image,(50,50),50,(0,0,255),-1)
cv2.circle(image,(50,460),50,(0,0,255),-1)
cv2.circle(image,(460,460),50,(0,0,255),-1)
cv2.circle(image,(460,50),50,(0,0,255),-1)

font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,'hello',(100,350),font,4,(10,56,167))

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
