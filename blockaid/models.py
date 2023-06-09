from django.db import models
from django.contrib.auth.models import User


class Color(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    torso_color = models.CharField(max_length=7)
    pockets_color = models.CharField(max_length=7)
    left_sleeve_color = models.CharField(max_length=7)
    right_sleeve_color = models.CharField(max_length=7)