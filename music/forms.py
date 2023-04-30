from django import forms
from .models import ArtistBoard, TrackBoard

class ArtistAnswerForm(forms.ModelForm):
    class Meta:
        model = ArtistBoard
        fields = ["content"]
        labels = {
            "content": "답변 내용"
        }

class TrackAnswerForm(forms.ModelForm):
    class Meta:
        model = TrackBoard
        fields = ["content"]
        labels = {
            "content": "답변 내용"
        }