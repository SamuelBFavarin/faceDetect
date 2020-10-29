import cv2


class Recognizer:

    datasets_xml = {
        'frontal_faces_alt': "datasets/haarcascade_frontalface_alt.xml",
        'eyes': "datasets/haarcascade_eye.xml"
    }

    def training(self, object_type):

        try:
            xml_data_set_file = None

            if (str.upper(object_type) in ['EYE', 'EYES']):
                xml_data_set_file = self.datasets_xml['eyes']

            elif (str.upper(object_type) in ['FACE', 'FACES']):
                xml_data_set_file = self.datasets_xml['frontal_faces_alt']

            return cv2.CascadeClassifier(xml_data_set_file)

        except Exception as e:
            print(e)

    def detectObjects(self, model, frame):

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        objects = model.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        return objects
