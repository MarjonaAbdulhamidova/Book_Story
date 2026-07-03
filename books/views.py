from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Author, Publisher, Book
from .serializers import (
    CategorySerializer, AuthorSerializer,
    PublisherSerializer, BookListSerializer, BookDetailSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    """Kategoriyalar — CRUD operatsiyalari"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']


class AuthorViewSet(viewsets.ModelViewSet):
    """Mualliflar — CRUD operatsiyalari"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'country', 'biography']
    ordering_fields = ['full_name', 'birth_date']


class PublisherViewSet(viewsets.ModelViewSet):
    """Nashriyotlar — CRUD operatsiyalari"""
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email']
    ordering_fields = ['name']


class BookViewSet(viewsets.ModelViewSet):
    """
    Kitoblar — to'liq CRUD + filter + search + pagination.

    **Filter parametrlari:**
    - `category` — kategoriya ID si
    - `author` — muallif ID si
    - `publisher` — nashriyot ID si
    - `language` — til (Uzbek, Russian, English)
    - `is_available` — mavjudligi (true/false)
    - `publish_year` — nashr yili

    **Search:** `?search=kitob nomi`

    **Ordering:** `?ordering=price` yoki `?ordering=-created_at`
    """
    queryset = Book.objects.select_related('author', 'category', 'publisher').all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'author', 'publisher', 'language', 'is_available', 'publish_year']
    search_fields = ['title', 'author__full_name', 'isbn', 'description']
    ordering_fields = ['title', 'price', 'publish_year', 'created_at', 'stock']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookDetailSerializer