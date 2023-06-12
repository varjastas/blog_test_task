from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, TagViewSet, BlogsByTagView

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('blogs-by-tag/<str:tag_name>/', BlogsByTagView.as_view(), name='blogs-by-tag'),
    path('blogs/<int:pk>/', BlogViewSet.as_view({'get': 'retrieve'}), name='blog-detail-api'),
]   