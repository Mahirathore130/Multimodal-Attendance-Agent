
from backend.core.teaching_suggestions import TeachingSuggestionEngine

engine = TeachingSuggestionEngine()

session_data = {
    "engagement_scores": [75, 82, 35, 32],
    "audio_levels_dbfs": [-15, -18, -22, -16],
    "speech_activity": [True, True, False, True]
}

suggestions = engine.generate_suggestions(session_data)

print("Teaching suggestions:")
for suggestion in suggestions:
    print(suggestion)
