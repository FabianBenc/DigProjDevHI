from django.urls import path
from blockaid import views
from .views import save_colors
from .views import my_colors_view
from .views import post_design
from .views import remove_design

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path('save-colors/', save_colors, name = 'save_colors'),
    path('my-colors/', my_colors_view, name = 'my_colors'),
    path('post-design/', post_design, name = 'post_design'),
    path('remove-design/', remove_design, name = 'remove_design'),
    #path('hoodie-designer/', my_colors_view, name = 'my_colors'),
]
