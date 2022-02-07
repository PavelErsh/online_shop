from django.urls import path 
#from games.views import home
from games.views import GameListVieW

urlpatterns = [
path('', GameListVieW.as_view(), name='home')
        ]
