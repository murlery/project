from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from tattoos.models import Tattoo
from django.views.generic import TemplateView

# Create your views here.

class ShowTattoosView(TemplateView):
    template_name = "tattoos/show_tattoos.html"

    def get_context_data(self, **kwargs: Any) -> dict[str,Any]:
        context = super().get_context_data(**kwargs)
        context['tattoos'] = Tattoo.objects.all()
        return context
    

