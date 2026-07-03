
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, AuthorViewSet, PublisherViewSet, BookViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('authors', AuthorViewSet, basename='author')
router.register('publishers', PublisherViewSet, basename='publisher')
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]