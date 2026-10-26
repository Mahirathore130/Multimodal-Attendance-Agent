
class StudentAnalytics:
    """Generate a reflective analytics summary for one student."""

    def generate_summary(self, student_id, attendance, engagement_scores):
        scores = [
            max(0.0, min(100.0, float(score)))
            for score in engagement_scores
        ]

        # Calculate engagement statistics.
        if scores:
            average = sum(scores) / len(scores)
            lowest = min(scores)
            highest = max(scores)

            # Population standard deviation measures score variation.
            variance = sum(
                (score - average) ** 2 for score in scores
            ) / len(scores)
            variation = variance ** 0.5

            if variation <= 10:
                consistency = "Consistent"
            elif variation <= 20:
                consistency = "Moderately variable"
            else:
                consistency = "Highly variable"

            if average >= 70:
                trend = "Generally high engagement"
            elif average >= 40:
                trend = "Moderate engagement"
            else:
                trend = "Lower measured engagement"

            peak_periods = [
                index + 1 for index, score in enumerate(scores)
                if score >= 80
            ]
            low_periods = [
                index + 1 for index, score in enumerate(scores)
                if score < 40
            ]
        else:
            average = None
            lowest = None
            highest = None
            variation = None
            consistency = "Insufficient data"
            trend = "Insufficient data"
            peak_periods = []
            low_periods = []

        # Attendance values are supplied by the caller.
        present = bool(attendance.get("present", False))
        duration_seconds = max(
            0.0, float(attendance.get("presence_duration", 0.0))
        )

        return {
            "student_id": student_id,
            "attendance": {
                "present": present,
                "presence_duration_seconds": round(duration_seconds, 2)
            },
            "engagement": {
                "average_score": (
                    round(average, 2) if average is not None else None
                ),
                "lowest_score": lowest,
                "highest_score": highest,
                "score_variation": (
                    round(variation, 2)
                    if variation is not None else None
                ),
                "consistency": consistency,
                "overall_trend": trend,
                "high_engagement_periods": peak_periods,
                "low_engagement_periods": low_periods,
                "period_numbering": "One-based order of supplied scores"
            },
            "reflection": (
                "Review the periods of higher and lower measured "
                "engagement to reflect on your participation."
                if scores else
                "Collect engagement data before generating a reflection."
            )
        }
