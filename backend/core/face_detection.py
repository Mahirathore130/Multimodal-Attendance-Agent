import cv2
import os

class FaceDetector:
    def __init__(self):
        cascade_path = os.path.join (
            cv2.data.haarcascades
            + "haarcascade_frontalface_default.xml"
        )
        print("Cascade path:", cascade_path)
        print("File exists:", os.path.isfile(cascade_path))
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

        if self.face_cascade.empty():
            raise RuntimeError(
                "Could not load face cascade XML."
                "Check the OpenCV installation."
            )

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        detections = []

        for x, y, w, h in faces:
            detections.append({
                "bbox": (int(x), int(y), int(w), int(h)),
                "score": 1.0
            })

        return detections
