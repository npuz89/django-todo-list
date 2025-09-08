from django.urls import path #Импортируем path и views (представления, которые создадим дальше).
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'), #главная страница, обрабатывается функцией task_list.
    path('add/', views.add_task, name='add_task'), #страница для добавления задачи, обрабатывается функцией add_task.
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), #маршрут принимает ID задачи (например, /delete/1/ для задачи с ID=1).views.delete_task — представление, которое создадим дальше.name='delete_task' — имя маршрута для ссылок.
    path('edit/<int:task_id>', views.edit_task, name='edit_task'), #маршрут на редактирование
] #name - имя маршрута, чтобы ссылаться на него в коде.