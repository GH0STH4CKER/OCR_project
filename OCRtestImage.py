from cv2 import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C://Program Files (x86)//Tesseract-OCR//tesseract.exe"
url = "C:\\Users\\Dimuth De Zoysa\\Downloads\\hpbhealthgov.png"
img = cv2.imread(url)
img = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
#print(pytesseract.image_to_string(img))

#HIimg, WIimg, ZImg = img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
      b= b.split()
      print(b)
      if len(b) == 12:
        x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
        cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
        cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
        

cv2.imshow("OCR Text in Image",img)
cv2.waitKey(0)
