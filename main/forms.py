from django import forms
from .models import Feedback
from .models import Subscriber

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введите ваш email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема сообщения'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше сообщение...',
                'rows': 5
            }),
        }
        
        labels = {
            'name': 'Ваше имя',
            'email': 'Email адрес',
            'subject': 'Тема сообщения', 
            'message': 'Сообщение'
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш email'
            }),
        }
        
        labels = {
            'email': 'Email для подписки'
        }