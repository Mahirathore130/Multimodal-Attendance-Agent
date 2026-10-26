
class MultimodalAgent:
    """Combine vision, attendance, and audio metrics."""

    def analyze_session(
        self,
        attendance_data,
        audio_data,
        visual_engagement=0.0
    ):
        # Calculate the percentage of participants marked present.
        total_participants = len(attendance_data)

        if total_participants:
            present_count = sum(
                1 for record in attendance_data.values()
                if record.get("present", False)
            )
            attendance_rate = (
                present_count / total_participants
            ) * 100
        else:
            attendance_rate = 0.0

        # Read audio activity metrics.
        speech_active = audio_data.get("speech_active", False)
        rms = audio_data.get("rms", 0.0)
        noise_level = audio_data.get("level_dbfs")

        # Simple, explainable classroom interpretation.
        if visual_engagement >= 70 and speech_active:
            insight = "High visual engagement with active audio."
        elif visual_engagement >= 70:
            insight = "High visual engagement; little audio activity detected."
        elif speech_active:
            insight = "Audio activity detected; review visual engagement."
        else:
            insight = "Low measured activity; review the session context."

        return {
            "attendance_rate_percent": round(attendance_rate, 2),
            "visual_engagement": visual_engagement,
            "speech_active": bool(speech_active),
            "audio_rms": float(rms),
            "audio_level_dbfs": noise_level,
            "classroom_insight": insight
        }
