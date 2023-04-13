from django.urls import path
from blockaid import views
from blockaid.views import HomePageView, CreatePostView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/", CreatePostView.as_view(), name="add_post")  # new
]
