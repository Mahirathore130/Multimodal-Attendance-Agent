
import cv2
import numpy as np
from backend.core.face_detection import FaceDetector

detector = FaceDetector()

# Create a blank image with no face
image = np.zeros((480, 640, 3), dtype=np.uint8)

print("Testing an image with no face...")

detections = detector.process_frame(image)

print("Detected faces:", len(detections))

if len(detections) == 0:
    print("PASS: No face detected, and the system handled it correctly.")
else:
    print("CHECK: The detector returned false-positive detections.")

cv2.imshow("No Face Test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
