
from backend.core.student_analytics import StudentAnalytics

analytics = StudentAnalytics()

attendance = {
    "present": True,
    "presence_duration": 1500
}

engagement_scores = [65, 82, 75, 35, 88, 72]

result = analytics.generate_summary(
    student_id="student_1",
    attendance=attendance,
    engagement_scores=engagement_scores
)

print("Student Session Analytics:")
print(result)
