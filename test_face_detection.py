
import cv2
from backend.core.face_detection import FaceDetector

detector = FaceDetector()

image = cv2.imread("test_face.jpg")

if image is None:
    print("Image not found! Add test_face.jpg to the project folder.")
else:
    detections = detector.process_frame(image)
    print("Detected faces:", len(detections))

    for detection in detections:
        x, y, w, h = detection["bbox"]
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Detection Test", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
