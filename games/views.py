from django.shortcuts import render
from django.views.generic import ListView #для отображения страници в виде списка
from games.models import Game

class GameListVieW(ListView):
    model = Game #берём все записи
    template_name = 'games/home.html'#место в ктором находится наша стартовая страница
    content_text = 'game_list'#список всех наших игр в БД, мы его перемещяем в список content_text


# Create your views here.

def home(request):
    return render(request, 'home.html')
