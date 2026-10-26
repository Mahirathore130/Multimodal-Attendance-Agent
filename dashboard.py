
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Multimodal Attendance Agent",
    page_icon="📊",
    layout="wide"
)

st.title("Multimodal Attendance & Engagement Agent")
st.caption("Classroom session analytics demonstration")

# Demonstration data
attendance_data = pd.DataFrame([
    {"Student": "Student 1", "Present": "Yes", "Presence (minutes)": 25},
    {"Student": "Student 2", "Present": "Yes", "Presence (minutes)": 15},
    {"Student": "Student 3", "Present": "No", "Presence (minutes)": 0},
])

engagement_data = pd.DataFrame({
    "Session Period": ["Period 1", "Period 2", "Period 3", "Period 4"],
    "Engagement Score": [75, 82, 35, 68]
})

suggestions = [
    "Consider a short interactive activity during low-engagement periods.",
    "Review teaching approaches used during high-engagement periods.",
    "Check classroom conditions if audio levels remain high."
]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Participants", len(attendance_data))

with col2:
    present_count = (attendance_data["Present"] == "Yes").sum()
    st.metric("Present", int(present_count))

with col3:
    st.metric(
        "Average Engagement",
        f"{engagement_data['Engagement Score'].mean():.1f}/100"
    )

st.subheader("Attendance Records")
st.dataframe(attendance_data, use_container_width=True)

st.subheader("Engagement Timeline")
st.line_chart(
    engagement_data.set_index("Session Period")["Engagement Score"]
)

st.subheader("Teaching Suggestions")
for suggestion in suggestions:
    st.write(f"• {suggestion}")

with st.expander("Student Session Analytics"):
    st.write(
        "This demonstration summarizes attendance and engagement. "
        "Connect the actual analytics module to show real session results."
    )
    st.dataframe(engagement_data, use_container_width=True)

st.info(
    "Demonstration data only. This dashboard is not yet connected "
    "to live webcam or microphone output."
)
