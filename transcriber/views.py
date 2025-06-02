from django.shortcuts import render
from .forms import UploadAudioForm
from .whisper_gpt import transcribe_and_summarize

def upload_audio(request):
    transcript = summary = None

    if request.method == 'POST':
        form = UploadAudioForm(request.POST, request.FILES)
        if form.is_valid():
            audio = request.FILES['audio_file']
            transcript, summary = transcribe_and_summarize(audio)
    else:
        form = UploadAudioForm()

    return render(request, 'transcriber/upload.html', {
        'form': form,
        'transcript': transcript,
        'summary': summary
    })
