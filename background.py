#!/usr/bin/env python3
import cv2

cap = cv2.VideoCapture(0) # 0 -> webcam

while cap.isOpened():
    ret, back = cap.read() # reading from webcam 
    if ret:
        # if ret = True, camera works and is reading
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'): # ord -> returns the unicode value
            # this will save the image if user pressed 'q'
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
