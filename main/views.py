from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Lecture, Project, Feedback, Subscriber
from .forms import FeedbackForm, SubscribeForm 

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
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы ответим вам в ближайшее время.')
            return redirect('contacts')
    else:
        form = FeedbackForm()
    
    context = {
        'title': 'Контакты',
        'form': form
    }
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

def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    context = {
        'title': lecture.title,
        'lecture': lecture
    }
    return render(request, 'main/lecture_detail.html', context)

def feedback_list(request):
    if not request.user.is_staff:
        return redirect('home')
    
    feedbacks = Feedback.objects.all()
    context = {
        'title': 'Сообщения обратной связи',
        'feedbacks': feedbacks
    }
    return render(request, 'main/feedback_list.html', context)

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Вы успешно подписались на новости!')
                return redirect('subscribe_success')
            except:
                messages.error(request, 'Этот email уже подписан на новости.')
        else:
            messages.error(request, 'Пожалуйста, введите корректный email.')
    else:
        form = SubscribeForm()
    
    context = {'title': 'Подписаться на новости', 'form': form}
    return render(request, 'main/subscribe.html', context)

def subscribe_success(request):
    context = {'title': 'Подписка успешна'}
    return render(request, 'main/subscribe_success.html', context)

def unsubscribe(request, email):
    try:
        subscriber = Subscriber.objects.get(email=email)
        subscriber.is_active = False
        subscriber.save()
        message = f'Email {email} отписан от рассылки.'
    except Subscriber.DoesNotExist:
        message = 'Такой email не найден в списке подписчиков.'
    
    context = {'title': 'Отписка от рассылки', 'message': message}
    return render(request, 'main/unsubscribe.html', context)