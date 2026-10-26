
# Activity 6.3: Validate Outputs and Edge Cases

## Test Results

| Test Case | Expected Result | Actual Result |
|---|---|---|
| No face detected | Handles an empty frame without crashing | Passed — detected 0 faces |
| Lighting changes | Face detection works under different lighting | Passed — green rectangle and tracking ID visible in both bright and dim rooms |
| Partial face obstruction | Handles a partially covered face | Limitation observed — rectangle disappeared temporarily |
| Silence and background noise | Audio analysis handles silence and noise | Passed for generated signals — silence classified inactive and active test tone classified active; real background noise not tested |
| Short participant appearance | Attendance follows the 10-second threshold | Passed — absent before 10 seconds and present at 10 seconds |
| Engagement scoring | Score is within the range 0–100 | Passed — score 75.0, engagement level High |
| Signal fusion | Vision and audio timestamps are matched within 1 second | Passed — sync gaps of 0.5 seconds and 0.2 seconds |

## Issues and Improvements

- Face detection temporarily failed when part of the face was covered.
- Real-world background noise and live microphone behavior still require testing.
- Engagement scores are prototype estimates and have not been validated against real student engagement.

## Conclusion

The prototype passed the tested no-face, lighting, generated audio signal, attendance threshold, engagement scoring, and signal fusion checks. Partial face obstruction remains a limitation. Additional real-world testing is required before deployment.
