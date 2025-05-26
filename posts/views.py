from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'post/postsList.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(published=True)

class MyPosts(LoginRequiredMixin, PostList):
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class BasePostView(LoginRequiredMixin):
    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['encabezado'] = self.encabezado  # le pasamos el valor desde la subclase
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, error="El formulario no es válido."))

class PostCreate(BasePostView, CreateView):
    template_name = 'post/postForm.html'
    success_url = reverse_lazy('posts')
    encabezado = 'Crear Post'

class PostEdit(BasePostView, UpdateView):
    template_name = 'post/postForm.html'
    success_url = reverse_lazy('posts')
    encabezado = 'Editar Post'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/postDelete.html'
    success_url = reverse_lazy('posts')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    encabezado = 'Eliminar Post'

    def dispatch(self, request, *args, **kwargs):
        print("Método:", request.method)
        if self.get_object().author != request.user:
            return HttpResponseForbidden("No tienes permiso para eliminar este post.")
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("Eliminando post...")
        return super().delete(request, *args, **kwargs)
    
class PostDetails(DetailView):
    model = Post
    template_name = 'post/postDetails.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
