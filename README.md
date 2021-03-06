# Real-Time Face and Eyes Detector :raising_hand:!

This project uses OpenCV to detect faces and eyes in real time. When detected, we can make changes, replacing the detected objects for other images.

## How Run?

 Install all libraries in requirements.txt
 
 In a terminal, run this code:

    python3 run.py

Use these flags to modify the execution:

    --object_type='FACE' #use values like 'EYE' or 'FACE'
    --show_border=True  #use values like True or False
    --show_image=True #use values like True or False

To stop, press the Q key

## Examples
#### Detecting one face:
![enter image description here](https://github.com/SamuelBFavarin/faceDetect/blob/master/images/one_face.jpeg?raw=true) 

#### Detecting two faces, and replace with dog emoji :dog::
![enter image description here](https://github.com/SamuelBFavarin/faceDetect/blob/master/images/two_faces_with_objects.jpeg?raw=true)

#### Detecting eyes:
![enter image description here](https://github.com/SamuelBFavarin/faceDetect/blob/master/images/eyes.jpeg?raw=true)

#### Detecting eyes and replace with eyes emoji :eyes::

![enter image description here](https://github.com/SamuelBFavarin/faceDetect/blob/master/images/eyes_with_objects.jpeg?raw=true)
