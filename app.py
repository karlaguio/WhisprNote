import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY") 

#1. load audiofile
audio_file = open("example_audio.mp3", "rb")

#2. Transcribe with whisper 
transcript = openai.Audio.transcribe("whisper-1", audio_file)
text = transcript['text']
print("TRANSCRIPT:\n", text)

#3. Using openAi chatGPT summarize
summary_prompt = f"Summarize the following transcript into concise bullet-point notes:\n\n{text}"
summary_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": summary_prompt}]
)

summary = summary_response.choices[0].message['content']
print("\nSUMMARY:\n", summary)
