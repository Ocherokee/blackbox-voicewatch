import pyaudio
import wave
import datetime
import os

# Audio recording parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5  # Adjust as needed
AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'audio_raw')

def get_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        frames.append(stream.read(CHUNK))
    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    if not os.path.exists(AUDIO_DIR):
        os.makedirs(AUDIO_DIR)
    filename = f"session_{get_timestamp()}.wav"
    file_path = os.path.join(AUDIO_DIR, filename)

    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    print(f"Saved recording to {file_path}")
    return file_path

if __name__ == "__main__":
    record_audio()
