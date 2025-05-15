import openai
import sys
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

if len(sys.argv) < 2:
    print("Usage: python app.py <audio_file>")
    sys.exit(1)

audio_path = sys.argv[1]

with open(audio_path, "rb") as audio_file:
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    text = transcript['text']
    print("TRANSCRIPT:\n", text)

    summary_prompt = f"Summarize the following transcript into concise bullet-point notes:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": summary_prompt}]
    )

    summary = response.choices[0].message['content']
    print("\nSUMMARY:\n", summary)

    with open("summary.md", "w") as f:
        f.write(summary)
