
import cv2


class CameraService:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.cap = None
        self.is_running = False

    def start(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(self.camera_id)

        if not self.cap.isOpened():
            self.cap.release()
            self.cap = None
            raise RuntimeError("Could not open camera")

        self.is_running = True

    def stop(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

        self.is_running = False

    def get_frame(self):
        if self.is_running and self.cap is not None:
            ret, frame = self.cap.read()

            if ret:
                return frame

        return None
