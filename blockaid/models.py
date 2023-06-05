from django.db import models


class Color(models.Model):
    torso_color = models.CharField(max_length=7)
    pockets_color = models.CharField(max_length=7)
    left_sleeve_color = models.CharField(max_length=7)
    right_sleeve_color = models.CharField(max_length=7)