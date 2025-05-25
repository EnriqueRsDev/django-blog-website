from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'category',
        ]
        labels = {
            'title': 'Titulo',
            'content': 'Contenido',
            'category': 'Category',
        }