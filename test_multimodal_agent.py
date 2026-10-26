
from backend.core.multimodal_agent import MultimodalAgent

agent = MultimodalAgent()

attendance = {
    "student_1": {"present": True},
    "student_2": {"present": True},
    "student_3": {"present": False}
}

audio = {
    "speech_active": True,
    "rms": 0.12,
    "level_dbfs": -18.4
}

result = agent.analyze_session(
    attendance_data=attendance,
    audio_data=audio,
    visual_engagement=75
)

print("Multimodal session analysis:")
print(result)
