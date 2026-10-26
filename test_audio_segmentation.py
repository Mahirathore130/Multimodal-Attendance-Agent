
import numpy as np
from backend.core.audio_analysis import AudioAnalyzer

sample_rate = 16000
audio = np.zeros(sample_rate * 3, dtype=np.float32)

analyzer = AudioAnalyzer(sample_rate=sample_rate)
segments = analyzer.segment_audio(
    audio,
    chunk_seconds=1.0,
    start_time=0.0
)

print("Number of segments:", len(segments))

for segment in segments:
    print(
        f"Start: {segment['start_time']:.1f}s, "
        f"End: {segment['end_time']:.1f}s, "
        f"Samples: {len(segment['audio_data'])}"
    )
