from rest_framework import serializers
from .models import Book, Comment, BlogPost
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "text"]


class BlogPostSerializer(serializers.ModelSerializer):

    # Allow creating and updating blogposts
    comments = CommentSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = ["id", "title", "author", "content", "comments"]

    # Comment author must match the blogpost author
    def create(self, validated_data):
        comments_data = validated_data.pop("comments", [])
        blogpost = BlogPost.objects.create(**validated_data)

        for comment_data in comments_data:
            if comment_data["author"] != blogpost.author:
                raise serializers.ValidationError(
                    "Comment author must match the blogpost author."
                )
            Comment.objects.create(blogpost=blogpost, **comment_data)
        return blogpost

    def update(self, instance, validated_data):
        comments_data = validated_data.pop("comments", [])
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        for comment_data in comments_data:
            if comment_data["author"] != instance.author:
                raise serializers.ValidationError(
                    "Comment author must match the blogpost author."
                )
            Comment.objects.create(blogpost=instance, **comment_data)
        return instance
