from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comments, Likes, Redot


class UserSerializer(serializers.ModelSerializer):
    """
    User Serialize to Parse the User Model into Json
    """

    class Meta:
        model = User
        fields = ("id", "username")


class UserProfileSerializer(serializers.ModelSerializer):

    """
    User Profile Serializer, Nesting the User Serializer
    with a create function overidden to make sure User is
    Created Always before the UserProfile is Created.
    """

    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ("id", "user", "bio", "followers")

        def create(self, validated_data):
            user_data = validated_data.pop("user")
            user = User.objects.create(**user_data)
            profile = UserProfile.objects.create(user=user, **validated_data)
            return profile


class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer
    """

    redots = "RedotSerializer(many=True, read_only=True)"

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "content",
            "date_updated",
            "date_posted",
            "redots",
            "like_count",
            "comment_count",
            "redot_count",
        )


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Serializer
    """

    user = UserSerializer()

    class Meta:
        model = Comments
        fields = ("id", "user", "content", "date_created", "date_updated")


class LikeSerializer(serializers.ModelSerializer):
    """
    Like Serializer
    """

    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Likes
        fields = ("id", "post", "user", "date_liked")


class RedotSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Redot
        fields = ("id", "user", "post", "redot_date")
