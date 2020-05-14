import cv2 
import numpy as np 

def colors():

    #this will mark dark image
    img = np.zeros((480,640) ,dtype = np.uint8)
    cv2.imshow("Dark Image" , img)
    img = np.zeros((512 ,512,3) , dtype = np.uint8)

    #this will mark Blue image
    img[:] = 255,0,0
    cv2.imshow("Blue Image" , img)

    #this will mark Green image
    img[:] = 0,255,0
    cv2.imshow("Green Image" , img)

    #this will mark Blue image
    img[:] = 0,0,255
    cv2.imshow("Red Image" , img)

    if cv2.waitKey(0)&0xFF == ord('q'):
        cv2.destroyAllWindows()
    img[:] = 0,0,0


    img[95 : 155] = 255,0,0
    img[175 : 225] = 0,255,0
    img[245 : 305] = 0,0,255
    img[325 : 375] = 255,255,255

    cv2.imshow("Range defined color" , img)

    if cv2.waitKey(0)&0xFF == ord('q'):
        cv2.destroyAllWindows()

#----------------------line-----------------------

def lines():
    img = np.zeros((480,640,3) ,dtype = np.uint8)
    img[:] = 0,0,0

    cv2.line(img ,(0,0), (img.shape[1] ,img.shape[0]) ,(0,255,0) ,3)
    cv2.line(img ,(0,0), (400 ,200) ,(0,120,80) ,3)

    cv2.imshow("Range defined color" , img)

    if cv2.waitKey(0)&0xFF == ord('q'):
        cv2.destroyAllWindows()

#-----------------------rectange--------------------
def rectange():
    img = np.zeros((512 ,512,3) ,dtype =np.uint8)

    cv2.rectangle(img ,(0,0), (img.shape[1]//2 ,img.shape[0]//2) ,(155,120,120) ,3)
    cv2.rectangle(img ,(img.shape[1]//2 ,img.shape[0]//2), (500 ,500) ,(155,120,80) ,cv2.FILLED)

    cv2.imshow("Rectangles" , img)

    if cv2.waitKey(0)&0xFF == ord('q'):
        cv2.destroyAllWindows()

def circle():
    img = np.zeros((512 ,512,3) ,dtype =np.uint8)
    img = cv2.circle(img , (img.shape[0]//4 ,img.shape[1]//4) , 30 , (0,255,0) , 3)
    cv2.imshow("Circles" , img)

    if cv2.waitKey(0)&0xFF == ord('q'):
        cv2.destroyAllWindows()

def WriteText():
    img = np.zeros((512 ,512,3) ,dtype =np.uint8)
    file = open('Readme.md' ,'r')
    text = file.read()
    file.close()

    text = "Hello"
    img = cv2.putText(img ,text = text , org = (25,25) ,fontFace= cv2.FONT_HERSHEY_SIMPLEX ,fontScale=1 ,color = (200 ,124,43), thickness=1, )
    img = cv2.putText(img ,text = text , org = (25,52) ,fontFace= cv2.FONT_HERSHEY_SIMPLEX ,fontScale=0.8 ,color = (200 ,124,43), thickness=3, )
    
    cv2.imshow("Writing Text On pictue" , img)

    if cv2.waitKey(0)&0xFF == ord('q'):
        cv2.destroyAllWindows()
if __name__ == "__main__":
    colors()
    lines()
    rectange()
    circle()
    WriteText()