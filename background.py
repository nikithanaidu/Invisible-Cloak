import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,back=cap.read() #this is reading from the webcam
    if ret==True: #if it is able to capture, show the image
        cv2.imshow("image",back)
        if cv2.waitKey(5)==ord('q'):
            #save the image
            cv2.imwrite('image.jpg',back)
            break
cap.release()
cv2.destroyAllWindows()