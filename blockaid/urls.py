from django.urls import path
from blockaid import views
from .views import save_colors

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path('save-colors/', save_colors, name = 'save_colors'),
]
