from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'category',
            'published',
        ]
        labels = {
            'title': 'Titulo',
            'content': 'Contenido',
            'category': 'Category',
            'published': 'Mostrar en el feed',
        }