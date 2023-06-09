from django.urls import path
from blockaid import views
from .views import save_colors
from .views import my_colors_view

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path('save-colors/', save_colors, name = 'save_colors'),
    path('my-colors/', my_colors_view, name = 'my_colors'),
]
