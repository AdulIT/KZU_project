from django.shortcuts import render, redirect
from .models import City
# from .forms import TaskForm


def index(request):
	data = {
		'title': 'Главная страница',
	}
	return render(request, 'main/index.html', data)


def about(request):
	return render(request, 'main/about.html')

def city(request):
	return render(request, 'main/city.html')

