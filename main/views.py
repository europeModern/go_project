from django.shortcuts import render

def home(request):
    context = {'title': 'Главная страница'}
    return render(request, 'main/home.html', context)

def about(request):
    context = {'title': 'Обо мне'}
    return render(request, 'main/about.html', context)

def portfolio(request):
    projects = ["Проект 1", "Проект 2", "Проект 3"]
    context = {
        'title': 'Портфолио', 
        'projects': projects
    }
    return render(request, 'main/portfolio.html', context)
