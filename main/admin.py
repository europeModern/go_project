from django.contrib import admin
from .models import (
    Category, Project, Lecture, Feedback, Subscriber,
    Manufacturer, Product
)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_processed',)
    readonly_fields = ('created_at',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('email',)
    list_editable = ('is_active',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year', 'is_active', 'product_count')
    list_filter = ('country', 'is_active')
    search_fields = ('name', 'country')
    
    def product_count(self, obj):
        return obj.product_set.count()
    product_count.short_description = 'Количество товаров'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'manufacturer', 
        'category',
        'price', 
        'stock_quantity', 
        'is_available', 
        'created_at'
    )
    list_filter = ('manufacturer', 'category', 'is_available', 'created_at')
    search_fields = ('name', 'description', 'manufacturer__name', 'category__name')
    list_editable = ('price', 'stock_quantity', 'is_available')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'manufacturer', 'category')
        }),
        ('Цены и наличие', {
            'fields': ('price', 'stock_quantity', 'is_available')
        }),
        ('Дополнительная информация', {
            'fields': ('warranty_months', 'created_at')
        }),
    )
    actions = ['make_available', 'make_unavailable']
    
    def make_available(self, request, queryset):
        updated = queryset.update(is_available=True)
        self.message_user(request, f'{updated} товаров теперь доступны для продажи')
    make_available.short_description = "Сделать доступными для продажи"
    
    def make_unavailable(self, request, queryset):
        updated = queryset.update(is_available=False)
        self.message_user(request, f'{updated} товаров сняты с продажи')
    make_unavailable.short_description = "Снять с продажи"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_count', 'description_short')
    search_fields = ('name', 'description')
    
    def product_count(self, obj):
        return obj.product_set.count()
    product_count.short_description = 'Количество товаров'
    
    def description_short(self, obj):
        if len(obj.description) > 50:
            return obj.description[:50] + '...'
        return obj.description
    description_short.short_description = 'Описание (кратко)'