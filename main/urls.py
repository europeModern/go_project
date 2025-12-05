from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contacts/', views.contacts, name='contacts'),
    path('lectures/', views.lectures, name='lectures'),
    path('portfolio/<int:project_id>/', views.project_detail, name='project_detail'),
    path('lectures/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribe/success/', views.subscribe_success, name='subscribe_success'),
    path('unsubscribe/<str:email>/', views.unsubscribe, name='unsubscribe'),
]
