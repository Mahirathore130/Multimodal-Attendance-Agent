
class EngagementScorer:
    """Calculate an explainable engagement score from fused signals."""

    def calculate_score(self, fused_record):
        # Visual engagement is expected to be between 0 and 100.
        visual_score = max(
            0.0,
            min(100.0, float(
                fused_record.get("visual_engagement", 0.0)
            ))
        )

        # Presence duration contributes up to 100 points.
        presence_duration = max(
            0.0,
            float(fused_record.get("presence_duration", 0.0))
        )
        presence_score = min(100.0, presence_duration / 60.0 * 100)

        # Audio activity contributes 100 when detected, otherwise 0.
        audio_score = (
            100.0 if fused_record.get("speech_active", False)
            else 0.0
        )

        # Transparent weights: visual 50%, presence 30%, audio 20%.
        score = (
            visual_score * 0.50
            + presence_score * 0.30
            + audio_score * 0.20
        )

        score = round(score, 2)

        if score >= 70:
            level = "High"
        elif score >= 40:
            level = "Moderate"
        else:
            level = "Low"

        return {
            "engagement_score": score,
            "engagement_level": level,
            "components": {
                "visual_score": round(visual_score, 2),
                "presence_score": round(presence_score, 2),
                "audio_score": round(audio_score, 2)
            }
        }
