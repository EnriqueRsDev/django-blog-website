from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Category
from .forms import CategoryForm


# Create your views here.
class CategoryList(ListView):
    model = Category
    template_name = 'category/categoriesList.html'
    context_object_name = 'categories'
    ordering = ['name']

class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/categoryCreate.html'
    success_url = reverse_lazy('category')
