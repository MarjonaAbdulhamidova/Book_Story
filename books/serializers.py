
from rest_framework import serializers
from .models import Category, Author, Publisher, Book


class CategorySerializer(serializers.ModelSerializer):
    book_count = serializers.IntegerField(source='books.count', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'book_count', 'created_at']


class AuthorSerializer(serializers.ModelSerializer):
    book_count = serializers.IntegerField(source='books.count', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'full_name', 'biography', 'birth_date', 'country', 'photo', 'book_count']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address', 'phone', 'email', 'website']


class BookListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    publisher_name = serializers.CharField(source='publisher.name', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author_name', 'category_name', 'publisher_name',
            'price', 'language', 'publish_year', 'stock', 'is_available', 'cover_image',
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), source='publisher', write_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'description',
            'author', 'author_id',
            'category', 'category_id',
            'publisher', 'publisher_id',
            'price', 'pages', 'language', 'isbn',
            'publish_year', 'stock', 'max_readers',
            'cover_image', 'is_available',
            'created_at', 'updated_at',
        ]

    def validate_isbn(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("ISBN faqat raqamlardan iborat bo'lishi kerak.")
        if len(value) != 13:
            raise serializers.ValidationError("ISBN 13 ta raqamdan iborat bo'lishi kerak.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Narx 0 dan katta bo'lishi kerak.")
        return value