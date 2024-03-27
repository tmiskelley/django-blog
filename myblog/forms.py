from django import forms

from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('author', 'category', 'title', 'body')

    widgets = {
      'author': forms.Select(attrs={'class': 'form-select'}),
      'category': forms.Select(choices=choices, attrs={'class': 'form-select'}),
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }
