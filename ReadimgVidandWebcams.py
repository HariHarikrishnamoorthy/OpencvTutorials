#   Athour Hari
#   Read images Videos and Webcams

import cv2 
import numpy as np


def readImg():
    img = cv2.imread("Resources\lena.png")
    cv2.imshow("Title Name",img)
    cv2.waitKey(0)

def readVid():

    cap = cv2.VideoCapture("Resources\test_video.mp4")

    while True:
            #   this read funtion will read and return the (Succes <type bool>) which tells videos is playing , and img
        success , img = cap.read()
        if not success:
            break
    
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
    #readVid()
    readWebcam()
