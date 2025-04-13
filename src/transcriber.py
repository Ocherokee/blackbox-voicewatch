import whisper
import sys

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    transcription = result.get("text", "").strip()
    return transcription

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        text = transcribe_audio(file_path)
        print("Transcription:")
        print(text)
    else:
        print("Usage: python transcriber.py <audio_file>")

