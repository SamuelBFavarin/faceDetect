import cv2
import sys
import dlib
import logging as log
import datetime as dt
from time import sleep


class FaceRecognizer:

    datasets_xml = {
        'frontal_faces': "datasets/haarcascade_frontalface_default.xml",
        'frontal_faces_alt': "datasets/haarcascade_frontalface_alt.xml",
        'smiles': "datasets/haarcascade_smile.xml", 
        'eyes': "datasets/haarcascade_eye.xml"
    }

    faceCascade = None
    video_capture = cv2.VideoCapture(0)

    img_original = cv2.imread("images/dog.png", cv2.IMREAD_UNCHANGED)

    menu = {
        'show_rectangle': True,
        'show_object': False
    }


    def training(self, xml_data_set_file=None):
        if xml_data_set_file == None:        
            xml_data_set_file = self.datasets_xml['frontal_faces_alt']

        
        self.faceCascade = cv2.CascadeClassifier(xml_data_set_file)
    
    def runRecognizator(self):

        while True:

            self.waitCameraOpen()

            frame = self.getCurrentFrame()
            faces = self.detectFaces(frame)

            self.manipulateFaces(faces,frame)
            
            self.drawInfos(frame, len(faces))         
            
            self.keyHasPressed()

            if self.endKeyHasPressed():
                return self.stopProgram()                
                                                
            self.displayFrame(frame)

    def manipulateFaces(self, faces, frame):
        
        for (pos_x, pos_y, width, height) in faces:

            face = {
                'pos_x': pos_x,
                'pos_y': pos_y,
                'width': width,
                'height': height,
                'init_position': (pos_x, pos_y),
                'end_position': (pos_x + width, pos_y + height)
            } 


            if self.menu['show_rectangle']:
                self.drawRectangle(face, frame)

            if self.menu['show_object']:
                self.drawImage(self.img_original, face, frame)

    def waitCameraOpen(self):
        if not self.video_capture.isOpened():
            print('Esperado 10 segundos para a camera abrir')
            sleep(10)
            pass

    def detectFaces(self, frame):
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.faceCascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        return faces

    def getCurrentFrame(self):
        ret, frame = self.video_capture.read()
        return frame


    def drawRectangle(self, face, frame):        
        GREEN_COLOR = (0, 255, 0)
        BORDER_SIZE = 3
        cv2.rectangle(frame, face['init_position'], face['end_position'], GREEN_COLOR, BORDER_SIZE)


    def drawImage(self, image, face, frame):
        dimension = (face['width'], face['height'])
        new_image = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)
        
        y1, y2 = face['pos_y'], face['pos_y']  + new_image.shape[0]
        x1, x2 = face['pos_x'], face['pos_x'] + new_image.shape[1]

        alpha_s = new_image[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s

        for c in range(0, 3):
            frame[y1:y2, x1:x2, c] = (alpha_s * new_image[:, :, c] + alpha_l * frame[y1:y2, x1:x2, c])

    def drawInfos(self, frame, num_faces):
        
        RED_COLOR = (0, 0, 255)
        FONT_SIZE = 0.5

        cv2.putText(frame, "Quantidade de objetos: " + str(num_faces), (20,20), cv2.FONT_HERSHEY_SIMPLEX, FONT_SIZE, RED_COLOR)
        cv2.putText(frame,"Tecle Q para sair", (20,40), cv2.FONT_HERSHEY_SIMPLEX, FONT_SIZE, RED_COLOR)

    def keyHasPressed(self):
        
        if cv2.waitKey(1) & 0xFF == ord('r'):
            self.showRectangle()
            
        elif cv2.waitKey(1) & 0xFF == ord('o'):
            self.showObject()

        elif cv2.waitKey(1) & 0xFF == ord('e'):                
            self.training(self.datasets_xml['eyes'])
            self.img_original = cv2.imread("images/eye.png", cv2.IMREAD_UNCHANGED)

        elif cv2.waitKey(1) & 0xFF == ord('h'):                
            self.training(self.datasets_xml['frontal_faces_alt'])
            self.img_original = cv2.imread("images/dog.png", cv2.IMREAD_UNCHANGED)


    def showRectangle(self):
        if self.menu['show_rectangle'] == True: 
            self.menu['show_rectangle'] = False
        else:
            self.menu['show_rectangle'] = True

    def showObject(self):
        if self.menu['show_object'] == True: 
            self.menu['show_object'] = False
        else:
            self.menu['show_object'] = True


    def endKeyHasPressed(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return True

        return False 

    def stopProgram(self):        
        self.video_capture.release()
        cv2.destroyAllWindows()
        return True

    def displayFrame(self, frame):
        cv2.imshow('Video', frame)


face_recognizer = FaceRecognizer()
face_recognizer.training()
face_recognizer.runRecognizator()