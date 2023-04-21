from django.db import models


class Post(models.Model):
    description = models.TextField()
    choose = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title