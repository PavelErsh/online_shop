from django.db import models
from django.contrib.auth import get_user_model#Подключаем модель пользователя

# Create your models here.
class Game(models.Model):
    title = models.TextField(max_length=50)#Создаём текстовое поле для названия игры
    description = models.TextField()#Создаём поле для описания игры которое не ограничено по длинне
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)#Поле владелец которое является ключевым и в него передаём  готовую модель пользователя, так же указываем, что при удалении пользователя будут удаляться и его записи
    slug = models.SlugField(unique=True)#это поле нужно для генерации уникальных URL в строке браузера
    price = models.DecimalField(max_digits = 6, decimal_places = 2) #поле цены у которово количество знаков до точки не более 6, а после точки не более 2
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)
    #поля created и updated автоматически наполняются необходимыми данными
    image = models.ImageField(blank=True)#image
    
    def __str__(self):#Функция для того что бы были видны названия наших игр
        return f'{self.title}'


