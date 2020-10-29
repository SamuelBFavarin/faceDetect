import cv2
from time import sleep


class Interface:

    img = None
    show_border = None
    show_image = None

    def startVideoCapture(self, object_type, show_border, show_image):

        if (str.upper(object_type) in ['EYE', 'EYES']):
            self.img = cv2.imread(
                "images/eye.png", cv2.IMREAD_UNCHANGED)

        elif (str.upper(object_type) in ['FACE', 'FACES']):
            self.img = cv2.imread(
                "images/dog.png", cv2.IMREAD_UNCHANGED)

        self.show_border = show_border
        self.show_image = show_image

        return cv2.VideoCapture(0)

    def waitCameraOpen(self, video_capture):
        if not video_capture.isOpened():
            print('Waiting camera for 10 seconds')
            sleep(10)
            pass

    def getCurrentFrame(self, video_capture):
        _, frame = video_capture.read()
        return frame

    def displayFrame(self, frame):
        cv2.imshow('Video', frame)

    def drawObjects(self, objects, frame):

        for (pos_x, pos_y, width, height) in objects:

            obj = {
                'pos_x': pos_x,
                'pos_y': pos_y,
                'width': width,
                'height': height,
                'init_position': (pos_x, pos_y),
                'end_position': (pos_x + width, pos_y + height)
            }

            if self.show_border:
                self.__drawRectangle(obj, frame)

            if self.show_image:
                self.__drawImage(self.img, obj, frame)

        self.__drawInfos(frame, len(objects))

    def __drawRectangle(self, obj, frame):
        GREEN_COLOR = (0, 255, 0)
        BORDER_SIZE = 3
        cv2.rectangle(frame, obj['init_position'],
                      obj['end_position'], GREEN_COLOR, BORDER_SIZE)

    def __drawImage(self, image, obj, frame):
        dimension = (obj['width'], obj['height'])
        new_image = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)

        y1, y2 = obj['pos_y'], obj['pos_y'] + new_image.shape[0]
        x1, x2 = obj['pos_x'], obj['pos_x'] + new_image.shape[1]

        alpha_s = new_image[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s

        for c in range(0, 3):
            frame[y1:y2, x1:x2, c] = (
                alpha_s * new_image[:, :, c] + alpha_l * frame[y1:y2, x1:x2, c])

    def __drawInfos(self, frame, num_objects):

        RED_COLOR = (0, 0, 255)
        FONT_SIZE = 0.5

        cv2.putText(frame, "Number of objects: " + str(num_objects),
                    (20, 20), cv2.FONT_HERSHEY_SIMPLEX, FONT_SIZE, RED_COLOR)

        cv2.putText(frame, "Type Q to exit", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, FONT_SIZE, RED_COLOR)
