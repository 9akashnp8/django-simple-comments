from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Comment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class CommentSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = [
            "content",
            "created_at",
            "author",
        ]
