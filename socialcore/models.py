from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=255, blank=True, null=True)
    followers = models.ManyToManyField(User, related_name="following", blank=True)

    @property
    def follower_count(self):
        return self.followers.count()

    @property
    def following(self):
        return self.user.following.all()


class Post(models.Model):
    content = models.CharField(max_length=800)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    date_posted = models.DateField(auto_created=True)
    date_updated = models.DateField(auto_now_add=True)
    redots = models.ManyToManyField(
        User, through="Redot", related_name="retweeted_posts"
    )

    @property
    def like_count(self):
        return self.post_liked.count()

    @property
    def comment_count(self):
        return self.post_commented.count()

    @property
    def redot_count(self):
        return self.redot_posts.count()


class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_commented"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_commented"
    )
    content = models.CharField(max_length=300)
    date_commented = models.DateField(auto_created=True)
    date_updated = models.DateField(auto_now_add=True)


class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_liked")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_liked")
    date_liked = models.DateField(auto_now_add=True)


class Redot(models.Model):  # Redot is just like retweeting in my DotSocial App
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="redot_actions"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="redot_posts")
    redot_date = models.DateField(auto_now_add=True)
