from django.urls import path

from .views import homePageView, telegramView

urlpatterns = [
    path('', homePageView, name='home'),
    path('telegram', telegramView, name='telegram')
]
