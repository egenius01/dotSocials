from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comments, Likes, Redot
from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    PostSerializer,
    CommentSerializer,
    LikeSerializer,
    RedotSerializer,
)

from django.db.models import Q


class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["Post"])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"username": user.username},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSets(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            user_profile = UserProfile.objects.get(user=pk)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "user profile does not exist"}, status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk):
        try:
            user_profile = UserProfile.objects.get(user=pk)
            serializer = UserProfileSerializer(
                user_profile, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "user profile does not exist"}, status.HTTP_404_NOT_FOUND
            )


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        # user = self.request.user
        # following_users = UserProfile.objects.get(user=user).followers.all()
        # return Posts.objects.filter(Q(user__in=following_users) | Q(user=user))
        return Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        return Comments.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs["post_id"]
        post = Post.objects.get(id=post_id)
        serializer.save(user=self.request.user, post=post)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        return Likes.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs["post_id"]
        post = Post.objects.get(post_id=post_id)
        serializer.save(user=self.request.user, post=post)


class RedotViewSet(viewsets.ModelViewSet):
    serializer_class = RedotSerializer

    def get_queryset(self):
        user = self.request.user
        return Redot.objects.filter(user=user)

    def perform_create(self, serializer):
        post_id = self.kwargs["post_id"]
        post = Post.objects.get(post_id=post_id)
        serializer.save(user=self.request.user, post=post)
