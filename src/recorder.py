import pyaudio
import wave
import os
from datetime import datetime

# Config
AUDIO_DIR = "../data/audio_raw/"
FILENAME_PREFIX = "session"
CHANNELS = 1
RATE = 44100
CHUNK = 1024
FORMAT = pyaudio.paInt16
RECORD_SECONDS = 5

def record_audio(session_id, file_index, phrase_label="input"):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{FILENAME_PREFIX}_{session_id}_{file_index}_{phrase_label}_{now}.wav"
    filepath = os.path.join(AUDIO_DIR, filename)

    if not os.path.exists(AUDIO_DIR):
        os.makedirs(AUDIO_DIR)

    print(f"Recording for {RECORD_SECONDS} seconds...")

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filepath, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Saved: {filepath}")
    return filepath

if __name__ == "__main__":
    record_audio("001", "01", "zuo_de_hao")

