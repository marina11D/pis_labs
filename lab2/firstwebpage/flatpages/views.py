from django.shortcuts import render
from django.http import HttpResponse # импортируем класс HttpResponse, чтобы создавать ответы на запросы

def home(request):
    return render(request, 'static_handler.html')  # Показываем шаблон static_handler.html