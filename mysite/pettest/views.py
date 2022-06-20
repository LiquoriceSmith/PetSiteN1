from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.


class HomePettest(ListView):
    template_name = 'pettest/home_page.html'

    def get_queryset(self):
        return '1'
