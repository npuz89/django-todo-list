from django import forms 
from .models import Task

class TaskForm(forms.ModelForm): #TaskForm — форма, основанная на модели Task.
    class Meta:
        model = Task
        fields = ['title', 'completed'] #включаем только поля title и completed (поле created_at заполняется автоматически).
        labels = {
            'title': 'Название задачи',
            'completed':"Выполнена",
        } #В Meta добавили словарь labels, где: 'title': 'Название задачи' — задаёт метку для поля title 'completed': 'Выполнено' — задаёт метку для поля completed.
