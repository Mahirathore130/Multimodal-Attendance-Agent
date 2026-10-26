
import librosa
import numpy as np


class AudioAnalyzer:
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate

    def analyze_audio_chunk(self, audio_data):
        """Extract basic features from audio bytes or a NumPy array."""
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

            duration = len(audio) / self.sample_rate

            rms = librosa.feature.rms(y=audio)[0]
            zero_crossing_rate = (
                librosa.feature.zero_crossing_rate(y=audio)[0]
            )

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

    def segment_audio(
        self, audio_data, chunk_seconds=1.0, start_time=0.0
    ):
        """Split audio into fixed-duration segments with timestamps."""
        audio = np.asarray(audio_data, dtype=np.float32)

        if audio.size == 0 or chunk_seconds <= 0:
            return []

        chunk_size = int(self.sample_rate * chunk_seconds)

        if chunk_size <= 0:
            return []

        segments = []

        for start in range(0, len(audio), chunk_size):
            chunk = audio[start:start + chunk_size]

            if chunk.size == 0:
                continue

            segment_start = start_time + start / self.sample_rate
            segment_end = (
                segment_start + len(chunk) / self.sample_rate
            )

            segments.append({
                "start_time": float(segment_start),
                "end_time": float(segment_end),
                "audio_data": chunk
            })

        return segments

    def analyze_speech_activity(self, audio_data):
        """Estimate signal energy and detect activity using a threshold."""
        audio = np.asarray(audio_data, dtype=np.float32)

        if audio.size == 0:
            return {
                "rms": 0.0,
                "peak_amplitude": 0.0,
                "speech_active": False
            }

        rms = float(np.sqrt(np.mean(audio ** 2)))
        peak = float(np.max(np.abs(audio)))

        # Simple energy threshold, not actual speech recognition.
        speech_active = rms >= 0.02

        return {
            "rms": rms,
            "peak_amplitude": peak,
            "speech_active": bool(speech_active)
        }

    def analyze_noise_level(self, audio_data):
        """Estimate digital signal level in dBFS."""
        audio = np.asarray(audio_data, dtype=np.float32)

        if audio.size == 0:
            return {"rms": 0.0, "level_dbfs": None}

        rms = float(np.sqrt(np.mean(audio ** 2)))

        # Digital silence has no finite dBFS value.
        level_dbfs = 20 * np.log10(rms) if rms > 0 else None

        return {
            "rms": rms,
            "level_dbfs": (
                float(level_dbfs) if level_dbfs is not None else None
            )
        }
