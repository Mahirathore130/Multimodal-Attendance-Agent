
import time


class AttendanceLogic:
    def __init__(self, minimum_seconds=10):
        self.minimum_seconds = minimum_seconds
        self.participants = {}

    def update_presence(self, participant_id, timestamp=None):
        if timestamp is None:
            timestamp = time.time()

        if participant_id not in self.participants:
            self.participants[participant_id] = {
                "first_seen": timestamp,
                "last_seen": timestamp,
                "presence_duration": 0.0,
                "present": False
            }

        record = self.participants[participant_id]

        # Accumulate time only when observations are close together.
        gap = timestamp - record["last_seen"]

        if gap >= 0 and gap <= 2:
            record["presence_duration"] += gap

        record["last_seen"] = timestamp

        if record["presence_duration"] >= self.minimum_seconds:
            record["present"] = True

        return record.copy()

    def get_attendance(self):
        return {
            participant_id: record.copy()
            for participant_id, record in self.participants.items()
        }
