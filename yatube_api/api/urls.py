from rest_framework import routers
from rest_framework.authtoken import views

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                basename='comment')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
