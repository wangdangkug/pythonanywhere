from django.contrib import admin

from .models import Question, Choice , CinemaType , Cinema

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(CinemaType)
admin.site.register(Cinema)