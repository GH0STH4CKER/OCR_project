import numpy as np
from cv2 import cv2
import pytesseract

cap = cv2.VideoCapture(0)
pytesseract.pytesseract.tesseract_cmd = "C://Program Files (x86)//Tesseract-OCR//tesseract.exe"

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    
    boxes = pytesseract.image_to_data(gray)
    for x,b in enumerate(boxes.splitlines()):
        if x!=0:
          b= b.split()
          print(b)
          if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(gray,(x,y),(w+x,h+y),(0,0,255),3)
            cv2.putText(gray,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)   

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
#GHOSTH4CK3R
cv2.destroyAllWindows()
