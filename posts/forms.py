from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'category',
            'published',
        ]
        labels = {
            'title': 'Titulo',
            'content': 'Contenido',
            'image': 'Portada',
            'category': 'Category',
            'published': 'Mostrar en el feed',

        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-900 border border-gray-700 text-gray-200 focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-900 border border-gray-700 text-gray-200 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'rows': 6,
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-900 border border-gray-700 text-gray-200 focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'text-gray-200'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded'
            }),
        }