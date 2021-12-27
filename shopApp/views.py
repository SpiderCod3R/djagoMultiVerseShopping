from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = "index.html"