from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'post/postsList.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/newPost.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        # Puedes agregar mensajes, logs, o manipular el contexto
        return self.render_to_response(self.get_context_data(form=form, error="El formulario no es válido."))