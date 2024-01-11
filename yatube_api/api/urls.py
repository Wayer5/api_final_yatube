from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet,
)

router = DefaultRouter()
router.register(r'v1/posts', PostViewSet, basename='posts')
router.register(r'v1/groups', GroupViewSet, basename='groups')
router.register(r'v1/follow', FollowViewSet, basename='follow')
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
