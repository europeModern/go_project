from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Lecture(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название лекции')
    description = models.TextField(verbose_name='Краткое описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Тема сообщения')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    is_processed = models.BooleanField(default=False, verbose_name='Обработано')
    
    def __str__(self):
        return f"{self.subject} от {self.name}"
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
        ordering = ['-created_at']

class Subscriber(models.Model):
    email = models.EmailField(verbose_name='Email', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        ordering = ['-created_at']