#   Athour Hari
#   Read images Videos and Webcams

import cv2 
import numpy as np
from time import sleep

def readImg():
    img = cv2.imread("Resources\lena.png")
    cv2.imshow("Title Name",img)
    cv2.waitKey(0)
count =0 
def readVid():
    path = "Resources/test_video.mp4"
    #path = "D:/videoplayback (1).mp4"
    path = "D:/videoplayback.mp4"
    cap = cv2.VideoCapture(path)

    #Gitting Frames per second
    fps = cap.get(cv2.CAP_PROP_FPS) 

    #get total frame count 
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    #time period of the video is
    duration = float(frame_count)/float(fps)
    m = int(duration//60)
    s = duration %60

    time = 0
    count = 0
    
    while True:
            #   this read funtion will read and return the (Succes <type bool>) which tells videos is playing , and img
        success , img = cap.read()
        if not success:
            break
        width , height ,_ = np.shape(img)
        pos = (int(width*0.1) , int(height*0.47))

        count +=1 # count fps 
        if count == int(fps): #if count of fps in vid is equal to time is increased by 1:
            count = 0 
            time+=1
        minutes = time//60 
        seconds = time%60 

        hours = minutes//60 
        minutes = minutes%60

        display_time = "Time: "+str(hours)+"h:" +str(minutes)+"m:"+str(seconds)+"s"
        img = cv2.putText(img ,text = display_time , org = pos ,fontFace= cv2.FONT_HERSHEY_SIMPLEX ,fontScale=1,color = (0,0 ,0), thickness=2, )
        
        
        cv2.imshow("Name of video" , img)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            cv2.destroyAllWindows()
            break

def readWebcam():
    cap = cv2.VideoCapture(0)

    cap.set(3,640)          #0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
    cap.set(4,480)          #1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
    cap.set(10,200)         #2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
                            #3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
                            #4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
                            #5. CV_CAP_PROP_FPS Frame rate.
                            #6. CV_CAP_PROP_FOURCC 4-character code of codec.
                            #7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
                            #8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
                            #9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
                            #10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
                            #11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
                            #12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
                            #13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
                            #14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
                            #15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
                            #16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
                            #17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
                            #18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
    
    


    while True:
    
        success , img = cap.read()
        if not success:
            break
    
        cv2.imshow("Live Cam" , img)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    #readImg()
    readVid()
    #readWebcam()
