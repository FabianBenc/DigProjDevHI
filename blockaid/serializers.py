from rest_framework import serializers
from blockaid.models import Post

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title')