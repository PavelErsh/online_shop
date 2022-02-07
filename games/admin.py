from django.contrib import admin
from games.models import Game #Подключаем класс который написали в файле models.py
admin.site.register(Game) #Связваем админку с нашим классом
# Register your models here.


