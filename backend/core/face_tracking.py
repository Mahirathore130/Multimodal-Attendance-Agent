
from deep_sort_realtime.deepsort_tracker import DeepSort


class FaceTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)

    def update(self, detections, frame):
        """
        detections: list returned by FaceDetector.process_frame()
        frame: current video frame from OpenCV
        """
        tracker_inputs = []

        for detection in detections:
            x, y, w, h = detection["bbox"]
            confidence = detection.get("score", 1.0)

            tracker_inputs.append(
                ([x, y, w, h], confidence, "face")
            )

        tracks = self.tracker.update_tracks(
            tracker_inputs,
            frame=frame
        )

        results = []

        for track in tracks:
            if not track.is_confirmed():
                continue

            x1, y1, x2, y2 = map(
                int, track.to_ltrb()
            )

            results.append({
                "participant_id": str(track.track_id),
                "bbox": (x1, y1, x2 - x1, y2 - y1)
            })

        return results
