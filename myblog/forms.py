from django import forms

from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('author', 'title', 'body')

    widgets = {
      'author': forms.Select(attrs={'class': 'form-select'}),
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }
