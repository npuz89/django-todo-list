from django.db import models #импортируем модуль для работы с моделями.

class Task(models.Model): #создаём модель Task, которая наследуется от models.Model
    title = models.CharField(max_length=200) #поле для текста задачи, максимум 200 символов.
    completed = models.BooleanField(default=False) #булево поле (True/False), показывает, выполнена ли задача (по умолчанию False).
    created_at = models.DateTimeField(auto_now_add=True) #дата создания задачи, автоматически заполняется при создании.

    def __str__(self): #метод, чтобы в админке задачи отображались по заголовку
        return self.title



