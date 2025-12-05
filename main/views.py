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