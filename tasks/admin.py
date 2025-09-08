from django.contrib import admin
from .models import Task #Импортируем модель Task.
admin.site.register(Task) #Регистрируем её в админке, чтобы она появилась в интерфейсе.

# Register your models here.

