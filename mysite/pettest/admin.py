from django.contrib import admin
from .models import PetTest


# Register your models here.

class PetTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer1', 'answer2', 'answer3', 'right_answer')


admin.site.register(PetTest, PetTestAdmin)

admin.site.site_title = 'Управление тестами'
admin.site.site_header = 'Управление тестами'
