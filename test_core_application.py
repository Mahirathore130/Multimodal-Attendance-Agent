
from backend.core.multimodal_agent import MultimodalAgent
from backend.core.signal_fusion import SignalFusion
from backend.core.engagement_scoring import EngagementScorer
from backend.core.teaching_suggestions import TeachingSuggestionEngine
from backend.core.student_analytics import StudentAnalytics

def main():
    print("=== Multimodal Attendance & Engagement Agent ===")

    # Sample attendance data from the vision/attendance module.
    attendance = {
        "student_1": {
            "present": True,
            "presence_duration": 1500
        },
        "student_2": {
            "present": True,
            "presence_duration": 900
        }
    }

    # Sample timestamped visual observations.
    vision_data = [
        {
            "timestamp": 10.0,
            "participant_id": "student_1",
            "present": True,
            "presence_duration": 1500,
            "visual_engagement": 80
        },
        {
            "timestamp": 12.0,
            "participant_id": "student_2",
            "present": True,
            "presence_duration": 900,
            "visual_engagement": 60
        }
    ]

    # Sample audio observations from the audio module.
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

    # 1. Fuse vision and audio signals.
    fusion = SignalFusion()
    fused_records = fusion.fuse_signals(vision_data, audio_data)

    # 2. Calculate engagement scores.
    scorer = EngagementScorer()
    scored_records = []

    for record in fused_records:
        score_result = scorer.calculate_score(record)
        scored_record = {**record, **score_result}
        scored_records.append(scored_record)

    # 3. Generate a combined session insight.
    agent = MultimodalAgent()
    first_record = fused_records[0] if fused_records else {}

    session_insight = agent.analyze_session(
        attendance_data=attendance,
        audio_data=first_record,
        visual_engagement=first_record.get(
            "visual_engagement", 0
        )
    )

    # 4. Generate teaching suggestions from session metrics.
    suggestion_engine = TeachingSuggestionEngine()
    suggestions = suggestion_engine.generate_suggestions({
        "engagement_scores": [
            record["engagement_score"] for record in scored_records
        ],
        "audio_levels_dbfs": [
            record.get("audio_level_dbfs") for record in fused_records
        ],
        "speech_activity": [
            record.get("speech_active", False)
            for record in fused_records
        ]
    })

    # 5. Generate individual student analytics.
    analytics_engine = StudentAnalytics()
    student_summaries = {}

    for student_id, attendance_record in attendance.items():
        student_scores = [
            record["engagement_score"]
            for record in scored_records
            if record.get("participant_id") == student_id
        ]

        student_summaries[student_id] = analytics_engine.generate_summary(
            student_id=student_id,
            attendance=attendance_record,
            engagement_scores=student_scores
        )

    print("\nFused records:")
    for record in fused_records:
        print(record)

    print("\nEngagement scores:")
    for record in scored_records:
        print({
            "participant_id": record.get("participant_id"),
            "score": record["engagement_score"],
            "level": record["engagement_level"]
        })

    print("\nSession insight:")
    print(session_insight)

    print("\nTeaching suggestions:")
    for suggestion in suggestions:
        print(suggestion)

    print("\nStudent analytics:")
    for summary in student_summaries.values():
        print(summary)

    print("\nCore pipeline test completed.")

if __name__ == "__main__":
    main()
