from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    user_nama = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
    def get_user_nama(self, obj):
        if obj:
            return obj.username
        return None

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"