import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'phrases.json')

def load_fallback_phrases():
    with open(CONFIG_PATH, 'r') as f:
        data = json.load(f)
    return data.get("fallbacks", [])

def detect_glitch(transcription, response_text):
    fallback_phrases = load_fallback_phrases()

    if response_text in fallback_phrases:
        tag = "PR_INSERTION"
    elif not transcription and response_text:
        tag = "SILENT_GLITCH"
    elif response_text and response_text.rstrip().endswith(","):  # simplistic check for incomplete clause
        tag = "TRUNCATED_RESPONSE"
    elif "Transcript unavailable" in response_text:
        tag = "TRANSCRIPTION_FAIL"
    else:
        tag = "GENERIC_FILLER"
    return tag

if __name__ == "__main__":
    # Test example
    transcription = ""
    response_text = "Transcript unavailable due to error."
    tag = detect_glitch(transcription, response_text)
    print("Detected glitch tag:", tag)
