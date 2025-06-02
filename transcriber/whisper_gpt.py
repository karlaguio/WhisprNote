import openai
import tempfile
import whisper

openai.api_key = 'your-openai-api-key'

def transcribe_and_summarize(file):
    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        for chunk in file.chunks():
            tmp.write(chunk)
        temp_path = tmp.name

    model = whisper.load_model("base")
    result = model.transcribe(temp_path)
    transcript = result['text']
