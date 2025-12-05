from django.shortcuts import get_object_or_404, render
from .models import Lecture, Project

def home(request):
    context = {'title': 'Главная страница'}
    return render(request, 'main/home.html', context)

def about(request):
    context = {'title': 'Обо мне'}
    return render(request, 'main/about.html', context)

def portfolio(request):
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'title': 'Портфолио', 
        'projects': projects
    }
    return render(request, 'main/portfolio.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        context = {
            'title': 'Контакты',
            'success_message': f'Спасибо, {name}! Ваше сообщение отправлено.',
            'name': name,
            'email': email,
            'message': message
        }
    else:
        context = {'title': 'Контакты'}
    return render(request, 'main/contacts.html', context)

def lectures(request):
    lectures_list = Lecture.objects.all().order_by('-created_at')
    context = {
        'title': 'Лекции', 
        'lectures': lectures_list
    }
    return render(request, 'main/lectures.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'title': project.title,
        'project': project
    }
    return render(request, 'main/project_detail.html', context)