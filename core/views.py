from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.timezone import now


# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = now()
        return context
