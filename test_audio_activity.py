
import numpy as np
from backend.core.audio_analysis import AudioAnalyzer

analyzer = AudioAnalyzer(sample_rate=16000)

# Simulated silence
silence = np.zeros(16000, dtype=np.float32)

# Simulated loud signal
time_axis = np.arange(16000) / 16000
signal = 0.2 * np.sin(2 * np.pi * 440 * time_axis)

print("Silence:", analyzer.analyze_speech_activity(silence))
print("Active signal:", analyzer.analyze_speech_activity(signal))
