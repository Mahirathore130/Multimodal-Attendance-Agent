
from backend.core.signal_fusion import SignalFusion

fusion = SignalFusion()

vision_data = [
    {
        "timestamp": 10.0,
        "participant_id": "student_1",
        "present": True,
        "presence_duration": 30.0,
        "visual_engagement": 80
    },
    {
        "timestamp": 12.0,
        "participant_id": "student_2",
        "present": True,
        "presence_duration": 20.0,
        "visual_engagement": 60
    }
]

audio_data = [
    {
        "timestamp": 10.5,
        "speech_active": True,
        "rms": 0.12,
        "level_dbfs": -18.4
    },
    {
        "timestamp": 12.2,
        "speech_active": False,
        "rms": 0.01,
        "level_dbfs": -40.0
    }
]

result = fusion.fuse_signals(vision_data, audio_data)

for record in result:
    print(record)
