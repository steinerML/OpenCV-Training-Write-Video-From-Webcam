import cv2
#waitkey and escape character missing!!!!!!

#videocapture object for webcam capture (0=built-in cam, 1,2, etc for external)
vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
vid_capture.set(3,320) #Width
vid_capture.set(4,240) #Height
vid_capture.set(10,99) #Brightness
vid_capture.set(11,99) #Contrast

if(vid_capture.isOpened() == False):
	print("Error opening video stream")

# Obtain frame size information using get() method
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)
fps = 20

# Initialize video writer object
#AVI: cv2.VideoWriter_fourcc('M','J','P','G')
#MP4: cv2.VideoWriter_fourcc(*'XVID')
#DIVX MP4: cv2.VideoWriter_fourcc(*'DIVX')
#See table here: shorturl.at/dotBK

#output = cv2.VideoWriter('webcam_.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)
output = cv2.VideoWriter('webcam_.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 20, frame_size)


while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool 
    # and the second is frame
    ret, frame = vid_capture.read()
    
    if ret == True:
        # Write the frame to the output files
        output.write(frame)
        cv2.imshow("Frame",frame)
        key = cv2.waitKey(20)
        #k == 113 is ASCII code for q key. You can try to replace that 
		# with any key with its corresponding ASCII code, try 27 which is for ESCAPE
        if key == 27:
            break
    else:
        print('Webcam has been disconnected')
        break

# Release the objects
vid_capture.release()
output.release()
cv2.destroyAllWindows()
