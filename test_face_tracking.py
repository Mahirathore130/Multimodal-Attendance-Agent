
import cv2
from backend.core.face_detection import FaceDetector
from backend.core.face_tracking import FaceTracker

detector = FaceDetector()
tracker = FaceTracker()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam.")
    raise SystemExit(1)

print("Webcam started. Press Q to quit.")

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Could not read webcam frame.")
            break

        detections = detector.process_frame(frame)
        tracks = tracker.update(detections, frame)

        for track in tracks:
            x, y, w, h = track["bbox"]
            participant_id = track["participant_id"]

            cv2.rectangle(
                frame, (x, y), (x + w, y + h),
                (0, 255, 0), 2
            )
            cv2.putText(
                frame, f"ID: {participant_id}",
                (x, max(20, y - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 255, 0), 2
            )

        cv2.imshow("Face Detection and Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
