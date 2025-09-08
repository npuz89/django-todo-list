from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator #импортируем модуль пагинации.
from django.db.models import Q #импортируем для сложных запросов (хотя здесь используем простой фильтр).

def task_list(request):
    filter_status = request.GET.get('filter', 'all')# Получаем параметр фильтра получает параметр filter из URL (например, ?filter=completed). Если параметра нет, по умолчанию all.
    search_query = request.GET.get('search', '' ) ## Получаем поисковый запрос
    if request.method == 'POST': #Если запрос POST, получаем ID задачи из формы (task_id).
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id = task_id)
        task.completed = not task.completed #Находим задачу, переключаем её статус (not task.completed) и сохраняем.
        task.save()
        return redirect('task_list') #Перенаправляем на список задач.
    # Пагинация
    if filter_status == 'completed': #'completed' — только выполненные (completed=True).
        tasks = Task.objects.filter(completed=True)
    elif filter_status == 'incompleted':
        tasks = Task.objects.filter(completed=False) #'incomplete' — только невыполненные (completed=False).
    else:
        tasks = Task.objects.all() #получает все задачи из базы данных.
    # Поиск по заголовку
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    tasks = tasks.order_by('-created_at')

    paginator = Paginator(tasks, 5) #разбивает список задач на страницы по 5 задач.
    page_number = request.GET.get('page') #получает номер страницы из URL (например, ?page=2).
    page_obj = paginator.get_page(page_number) #объект страницы, который передаём в шаблон.
    return render(request, 'tasks/task_list.html', {
        'filter_status':filter_status, 
        'page_obj': page_obj,
        'search_query': search_query,}) #отображает шаблон передавая ему список задач.

def add_task(request):
    if request.method == 'POST': #Если запрос POST (форма отправлена), создаём форму с данными из запроса.
        form = TaskForm(request.POST)
        if form.is_valid(): #Если форма валидна (form.is_valid()), сохраняем задачу (form.save()) и перенаправляем на список задач (redirect('task_list')).
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form}) #Если запрос GET (просто открыли страницу), показываем пустую форму.

# Create your views here.

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id) #находит задачу по ID.
    task.delete() #удаляет задачу из базы данных.
    return redirect('task_list') #возвращает на главную страницу.

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task) #создаёт форму с данными текущей задачи для редактирования.
    return render(request, 'tasks/edit_task.html', {'form':form, 'task':task})
