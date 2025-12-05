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


class Manufacturer(models.Model):
    """
    Модель производителей оборудования
    """
    name = models.CharField(max_length=100, verbose_name='Название производителя')
    country = models.CharField(max_length=50, verbose_name='Страна')
    website = models.URLField(blank=True, verbose_name='Веб-сайт')
    founded_year = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        verbose_name='Год основания'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Основная модель продукции
    """
    name = models.CharField(max_length=200, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=models.PROTECT, 
        verbose_name='Производитель'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT, 
        verbose_name='Категория',
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Цена'
    )
    stock_quantity = models.PositiveIntegerField(
        default=0, 
        verbose_name='Количество на складе'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания'
    )
    is_available = models.BooleanField(
        default=True, 
        verbose_name='Доступен для продажи'
    )
    warranty_months = models.PositiveSmallIntegerField(
        default=12, 
        verbose_name='Гарантия (мес.)'
    )
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.manufacturer.name})"