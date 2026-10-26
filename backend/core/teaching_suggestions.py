
class TeachingSuggestionEngine:
    """Generate explainable teaching suggestions from session metrics."""

    def generate_suggestions(self, session_data):
        suggestions = []

        engagement = session_data.get("engagement_scores", [])
        audio_levels = session_data.get("audio_levels_dbfs", [])
        speech_activity = session_data.get("speech_activity", [])

        # 1. Identify sustained low engagement.
        if engagement:
            average = sum(engagement) / len(engagement)

            if average < 40:
                suggestions.append({
                    "type": "recommendation",
                    "message": (
                        "Consider adding an interactive activity, "
                        "question, or short discussion."
                    ),
                    "reason": (
                        f"Average engagement score was {average:.1f}/100."
                    )
                })

            # 2. Identify attention drops.
            if len(engagement) >= 2:
                for index in range(1, len(engagement)):
                    if (
                        engagement[index - 1] >= 60
                        and engagement[index] < 40
                    ):
                        suggestions.append({
                            "type": "recommendation",
                            "message": (
                                "Consider pausing to recap the topic "
                                "or check student understanding."
                            ),
                            "reason": (
                                f"Engagement dropped from "
                                f"{engagement[index - 1]} to "
                                f"{engagement[index]}."
                            )
                        })
                        break

            # 3. Highlight high-engagement periods.
            if max(engagement) >= 80:
                suggestions.append({
                    "type": "positive",
                    "message": (
                        "Review the high-engagement segment and "
                        "consider reusing its teaching approach."
                    ),
                    "reason": (
                        f"Peak engagement was {max(engagement)}/100."
                    )
                })

        # 4. Flag consistently high measured audio levels.
        high_noise_count = sum(
            1 for level in audio_levels
            if level is not None and level > -20
        )

        if audio_levels and high_noise_count / len(audio_levels) >= 0.5:
            suggestions.append({
                "type": "information",
                "message": (
                    "Check whether background noise is affecting "
                    "classroom communication."
                ),
                "reason": (
                    "At least half of the measured audio segments "
                    "were above -20 dBFS."
                )
            })

        # 5. Summarize detected speech activity.
        if speech_activity:
            active_count = sum(bool(value) for value in speech_activity)
            suggestions.append({
                "type": "information",
                "message": (
                    f"Audio activity was detected in "
                    f"{active_count} of {len(speech_activity)} segments."
                ),
                "reason": (
                    "This measures signal activity, not necessarily "
                    "speech or student participation."
                )
            })

        if not suggestions:
            suggestions.append({
                "type": "information",
                "message": (
                    "Collect more session data before making "
                    "a teaching recommendation."
                ),
                "reason": "There are not enough clear patterns yet."
            })

        return suggestions
