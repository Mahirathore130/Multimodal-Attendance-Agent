
from backend.core.attendance_logic import AttendanceLogic

attendance = AttendanceLogic(minimum_seconds=10)

for second in range(13):
    result = attendance.update_presence(
        participant_id="1",
        timestamp=100 + second
    )
    print(f"Time: {second}s | Record: {result}")

print("\nFinal attendance:")
print(attendance.get_attendance())
