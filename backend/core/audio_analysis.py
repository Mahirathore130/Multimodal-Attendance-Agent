
import librosa
import numpy as np


class AudioAnalyzer:
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate

    def analyze_audio_chunk(self, audio_data):
        """
        Analyze an audio chunk and return basic signal metrics.
        Input: raw 16-bit PCM bytes or a NumPy array.
        """
        
    def segment_audio(self, audio_data, chunk_seconds=1.0, start_time=0.0):
        """Split audio into fixed-duration chunks with timestamps."""
        audio = np.asarray(audio_data, dtype=np.float32)

        if audio.size == 0 or chunk_seconds <= 0:
            return []

        chunk_size = int(self.sample_rate * chunk_seconds)
        segments = []

        for start in range(0, len(audio), chunk_size):
            chunk = audio[start:start + chunk_size]

            if chunk.size == 0:
                continue

            timestamp = start_time + start / self.sample_rate

            segments.append({
                "start_time": float(timestamp),
                "end_time": float(timestamp + len(chunk) / self.sample_rate),
                "audio_data": chunk
            })

        return segments

        try:
            if isinstance(audio_data, bytes):
                audio = (
                    np.frombuffer(audio_data, dtype=np.int16)
                    .astype(np.float32) / 32768.0
                )
            else:
                audio = np.asarray(audio_data, dtype=np.float32)

            if audio.size == 0:
                return None

            # Resample if the input uses a different sample rate.
            # The input sample rate must be supplied by the caller.
            duration = len(audio) / self.sample_rate

            # Extract basic signal features.
            rms = librosa.feature.rms(y=audio)[0]
            zero_crossing_rate = librosa.feature.zero_crossing_rate(
                y=audio
            )[0]

            return {
                "sample_rate": self.sample_rate,
                "duration_seconds": float(duration),
                "amplitude_mean": float(np.mean(np.abs(audio))),
                "amplitude_max": float(np.max(np.abs(audio))),
                "rms_mean": float(np.mean(rms)),
                "zero_crossing_rate_mean": float(
                    np.mean(zero_crossing_rate)
                )
            }

        except (ValueError, TypeError) as error:
            print(f"Audio analysis error: {error}")
            return None
