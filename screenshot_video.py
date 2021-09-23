import cv2
import os
import time

def capture_images(inputFile, outputFile, step, counter):
    '''
    Inputs:
       inputFile = name of the input file (including directory)
       outputFile = name and file path for folder with the screenshots
       step = step between each image (in seconds)
       counter = number of screenshots 
    Output:
       counter many photos stored in the outputFile
    Example Call:
       capture_images('video.mp4', 'output', 20, 20)
    '''
    #insitalizing local
    step = step
    image_count = counter
    image_current = 0
    image_captured = 0

    #creating a folder
    try:
        if not os.path.exists(outputFile):
            os.makedirs(outputFile)
    #if not created throw error
    except OSError:
        print("Error: Could not create a directory!")

    #reading the video in
    video = cv2.VideoCapture(inputFile)

    #reading the number of frames at that second
    frames_per_sec = video.get(cv2.CAP_PROP_FPS)

    if video.isOpened():
        while(True):
            ret, image = video.read()
            if ret:
                #wait for step seconds of frame to go by befor you add another image
                if image_current > (step*frames_per_sec):
                    
                    image_current = 0
                    #name frame to be stored in specified directory
                    name =   outputFile + "/image" + str(image_captured) + ".jpg"
                    print("Creating " + name)
                    cv2.imwrite(name, image) 
                    ##if that text == prev of text
                    ##then if text is diff and ! empty then make new image
                    #number of images stored
                    image_captured+=1

                    if image_captured > (image_count + 1):
                        ret = False
                image_current+=1
            else:
                print("6")
                break
        #releasing space once done
        video.release()
        # cv2.distroyAllWindows()
    else:
        print("Not connected...")
#end capture_images