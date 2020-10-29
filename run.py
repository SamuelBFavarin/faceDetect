import cv2

from src.arguments import Arguments
from src.recognizer import Recognizer
from src.interface import Interface


class Main:

    recognizer = None
    model = None
    interface = None
    video_capture = None

    def __init__(self):
        self.recognizer = Recognizer()
        self.interface = Interface()

    def run(self, object_type, show_border, show_image):

        self.model = self.recognizer.training(object_type)
        self.video_capture = self.interface.startVideoCapture(
            object_type, show_border, show_image)

        while True:

            self.interface.waitCameraOpen(self.video_capture)

            frame = self.interface.getCurrentFrame(self.video_capture)
            objects = self.recognizer.detectObjects(self.model, frame)

            self.interface.drawObjects(objects, frame)

            if self.endKeyWasPressed():
                return self.stop()

            self.interface.displayFrame(frame)

    def endKeyWasPressed(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return True

        return False

    def stop(self):
        self.video_capture.release()
        cv2.destroyAllWindows()
        return True


if __name__ == "__main__":

    # get external arguments
    object_type, show_border, show_image = Arguments().setup()

    # start main
    main = Main()
    main.run(object_type, show_border, show_image)
