
class SignalFusion:
    """Combine timestamped vision and audio observations."""

    def fuse_signals(self, vision_data, audio_data):
        """
        vision_data: list of dictionaries containing timestamps
        and visual/attendance metrics.

        audio_data: list of dictionaries containing timestamps
        and audio metrics.
        """
        fused_records = []

        for vision in vision_data:
            vision_time = vision.get("timestamp", 0.0)

            # Match the audio observation closest in time,
            # provided it is within one second.
            matching_audio = None
            smallest_gap = float("inf")

            for audio in audio_data:
                audio_time = audio.get("timestamp", 0.0)
                gap = abs(vision_time - audio_time)

                if gap <= 1.0 and gap < smallest_gap:
                    matching_audio = audio
                    smallest_gap = gap

            if matching_audio is None:
                matching_audio = {}

            fused_records.append({
                "timestamp": vision_time,
                "participant_id": vision.get("participant_id"),
                "present": vision.get("present", False),
                "presence_duration": vision.get(
                    "presence_duration", 0.0
                ),
                "visual_engagement": vision.get(
                    "visual_engagement", 0.0
                ),
                "speech_active": matching_audio.get(
                    "speech_active", False
                ),
                "audio_rms": matching_audio.get("rms", 0.0),
                "audio_level_dbfs": matching_audio.get("level_dbfs"),
                "audio_timestamp": matching_audio.get("timestamp"),
                "sync_gap_seconds": (
                    smallest_gap if matching_audio else None
                )
            })

        return fused_records
