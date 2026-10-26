
from backend.core.engagement_scoring import EngagementScorer

scorer = EngagementScorer()

fused_record = {
    "timestamp": 10.0,
    "participant_id": "student_1",
    "present": True,
    "presence_duration": 30.0,
    "visual_engagement": 80,
    "speech_active": True,
    "audio_rms": 0.12,
    "audio_level_dbfs": -18.4
}

result = scorer.calculate_score(fused_record)

print("Engagement analysis:")
print(result)
