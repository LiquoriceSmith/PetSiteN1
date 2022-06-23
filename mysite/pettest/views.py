from django.shortcuts import render
from django.views.generic import ListView
from .models import PetTest, UserAnswer
from .forms import SimpleForm


# Create your views here.


class HomePettest(ListView):
    model = PetTest
    template_name = 'pettest/home_page.html'
    context_object_name = 'test'

    def get_queryset(self):
        return PetTest.objects.all()


def test(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['favorite_colors'])
            obj = UserAnswer()
            obj.user = 'Проверка'
            obj.answer = form.cleaned_data['favorite_colors']
            obj.save()
    else:
        form = SimpleForm()
    return render(request, 'pettest/test.html', {"form": form})
