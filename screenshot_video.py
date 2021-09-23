import cv2
import os
import time

def capture_images(inputFile, outputFile, step):
    '''
    Inputs:
        inputFile = name of the input file (including directory)
        outputFile = name and file path for folder with the screenshots
        step = time between each image/screenshot taken (in seconds) 
    Output:
        screenshots stored in the outputFile
    Example Call:
        capture_images('video.mp4', 'output', .5)
    '''
    #insitalizing local
    step = step
    images_captured = 1
    current_frame = 0
    frame_count = 0

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
    frames_total = video.get(cv2.CAP_PROP_FRAME_COUNT)

    if video.isOpened():
        while(True):
            ret, image = video.read()
            #increment counts
            current_frame+=1
            frame_count+=1
            
            #if end of video break
            if frame_count > frames_total:
                break

            #wait for step seconds of frame to go by befor you add another image
            if current_frame > (step*frames_per_sec):
                current_frame = 0
                #name frame to be stored in specified directory
                name =   outputFile + "/image" + str(images_captured) + ".jpg"
                print("Creating " + name)
                cv2.imwrite(name, image) 

                ##if that text == prev of text
                ##then if text is diff and ! empty then make new image

                #number of images stored
                images_captured+=1

        #releasing space once done
        video.release()
        cv2.distroyAllWindows()

    else:
        print("Not connected...")
        
#end capture_images