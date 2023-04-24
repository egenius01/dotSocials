from django.test import TestCase
from .models import User, UserProfile, Post
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTest(APITestCase):
    def test_create_user(self):
        url = reverse("user-register")
        data = {"username": "user1", "password": "randompassword"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserProfileTest(APITestCase):
    def setUp(self):
        # Create User Objects
        self.user1 = User.objects.create(username="user1", password="pass123")
        self.user2 = User.objects.create(username="user2", password="pass234")
        # create User Profiles
        # profile1
        self.userprofile1 = UserProfile.objects.create(user=self.user1, bio="balablue")
        # Set followers for user1:
        self.userprofile1.followers.set([self.user2])
        # profile2
        self.userprofile2 = UserProfile.objects.create(user=self.user2, bio="balablue2")

    def test_retrieve_user_profile(self):
        url = reverse("user-profile-detail", args=[self.userprofile1.id])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_profile(self):
        url = reverse("user-profile-detail", args=[self.userprofile1.id])
        data = {"bio": "I Have Decided to Run For Nigerain President"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="nuel", password="pass234")

    def test_create_post(self):
        url = reverse("post-list")
        # data
