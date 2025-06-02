from django import forms

class UploadAudioForm(forms.Form):
    audio_file = forms.FileField()

