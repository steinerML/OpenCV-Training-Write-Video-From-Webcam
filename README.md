# OpenCV Write Video from Webcam.
Writing video from laptop webcam using OpenCV.
## Contents:

In this the case I was reading from the laptop webcam using OpenCV.
I have used the following functions/methods:

| Function        |Action                                                                        | 
|----------------:|------------------------------------------------------------------------------|
|cv2.VideoCapture()   | Creates a video capture object, which would help stream or display the video.|
|**cv2.VideoWriter()**    | Saves the output video to a directory and takes 6 arguments.                 |
|     **filename**    |  Displays image.                                                             |
|    **apiPrefrence** |   API backends identifier                                                    |
|     **fourcc**      |  4-character code of codec, used to compress the frames                      |
|     **fps**         |  Frame rate of the created video stream                                      |
|     **frameSize**   |  Size of the video frames                                                    |
|     **isColor**     |  If not zero, the encoder will expect and encode color frames. Else it will work with grayscale frames.|


## Test Video used: 
In this case I haven't included the video due to privacy reasons.


## Summary:

```python
#Creates capture object, reading video from webcam
vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

```python
# Initialize video writer object
output = cv2.VideoWriter('Resources/output_video_from_file.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)

```
```python
# Initialize video writer object
output = cv2.VideoWriter('webcam_.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 20, frame_size)

```
