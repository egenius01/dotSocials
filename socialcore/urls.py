from django.urls import path, include
from rest_framework import routers
from .views import (
    LikeViewSet,
    PostViewSet,
    RedotViewSet,
    CommentViewSet,
    UserViewSet,
    UserProfileViewSets,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"userprofiles", UserProfileViewSets, basename="user-profile")
router.register(r"post", PostViewSet, basename="post")
router.register(r"like", LikeViewSet, basename="like")
router.register(r"redot", RedotViewSet, basename="redot")
router.register(r"comment", CommentViewSet, basename="comment")


urlpatterns = router.urls
