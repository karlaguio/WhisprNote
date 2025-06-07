#import the libraries
import openai
import tempfile
import whisper

openai.api_key = #need to add my key

def transcribe_and_summarize(file):
    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        for chunk in file.chunks():
            tmp.write(chunk)
        temp_path = tmp.name

    model = whisper.load_model("base")
    result = model.transcribe(temp_path)
    transcript = result['text']
#to summarize
    summary = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": f"Summarize this: {transcript}"}]
    )['choices'][0]['message']['content']

    return transcript, summary
