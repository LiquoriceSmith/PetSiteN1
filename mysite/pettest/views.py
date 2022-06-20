from django.shortcuts import render
from django.views.generic import ListView
from .models import PetTest

# Create your views here.


class HomePettest(ListView):
    model = PetTest
    template_name = 'pettest/home_page.html'
    context_object_name = 'test'

    def get_queryset(self):
        return PetTest.objects.all()
