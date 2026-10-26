
import numpy as np
from backend.core.audio_analysis import AudioAnalyzer

sample_rate = 16000
duration = 2

# Generate a two-second test tone.
time_axis = np.arange(sample_rate * duration) / sample_rate
audio = 0.5 * np.sin(2 * np.pi * 440 * time_axis)

analyzer = AudioAnalyzer(sample_rate=sample_rate)
result = analyzer.analyze_audio_chunk(audio)

print("Audio analysis result:")
print(result)
