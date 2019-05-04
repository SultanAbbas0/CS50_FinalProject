from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    word = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus','placeholder': 'learned a new word? type it down!', 'autocomplete':"off"}))
    meaning = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'what is the meaning of the word?', 'autocomplete':"off"}))
    sentence = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'put the word in a sentence', 'autocomplete':"off"}))
    refrence = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'where did you learn this word? (optional)', 'autocomplete':"off"}), required = False)

    class Meta:
        model = Word
        fields = ['word','meaning','sentence','refrence']
