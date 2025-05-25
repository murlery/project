from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from tournament.models import Tournament
# Create your views here.
class ShowTournamentsView(TemplateView):
    template_name = "tournaments/showTournaments.html"  # путь к шаблону

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tournaments = Tournament.objects.all()
        context['tournaments'] = tournaments
        return context
