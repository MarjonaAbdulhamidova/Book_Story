from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Author, Publisher, Book


class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
        self.category = Category.objects.create(name="Roman", description="Badiiy adabiyot")

    def test_category_list(self):
        res = self.client.get('/api/v1/categories/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_category_create_unauthorized(self):
        res = self.client.post('/api/v1/categories/', {'name': 'Yangi'})
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_create_authorized(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.post('/api/v1/categories/', {'name': 'Tarix', 'description': 'Tarixiy kitoblar'})
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_category_search(self):
        res = self.client.get('/api/v1/categories/?search=Roman')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'][0]['name'], 'Roman')


class AuthorTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
        self.author = Author.objects.create(
            full_name="Abdulla Qodiriy",
            country="Uzbekistan"
        )

    def test_author_list(self):
        res = self.client.get('/api/v1/authors/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_author_detail(self):
        res = self.client.get(f'/api/v1/authors/{self.author.id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['full_name'], 'Abdulla Qodiriy')

    def test_author_search(self):
        res = self.client.get('/api/v1/authors/?search=Qodiriy')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_author_delete_unauthorized(self):
        res = self.client.delete(f'/api/v1/authors/{self.author.id}/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class BookTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@test.com', 'admin123')

        self.category = Category.objects.create(name="Roman")
        self.author = Author.objects.create(full_name="Cho'lpon", country="Uzbekistan")
        self.publisher = Publisher.objects.create(name="Sharq")

        self.book = Book.objects.create(
            title="Kecha va Kunduz",
            description="Mashhur roman",
            author=self.author,
            category=self.category,
            publisher=self.publisher,
            price=25000,
            pages=320,
            isbn="9781234567890",
            publish_year=1936,
            stock=10,
        )

    def test_book_list(self):
        res = self.client.get('/api/v1/books/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['count'], 1)

    def test_book_detail(self):
        res = self.client.get(f'/api/v1/books/{self.book.id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'Kecha va Kunduz')

    def test_book_filter_by_category(self):
        res = self.client.get(f'/api/v1/books/?category={self.category.id}')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['count'], 1)

    def test_book_filter_by_language(self):
        res = self.client.get('/api/v1/books/?language=Uzbek')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_book_search(self):
        res = self.client.get('/api/v1/books/?search=Kecha')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'][0]['title'], 'Kecha va Kunduz')

    def test_book_create_authorized(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Yangi kitob',
            'description': 'Test kitob',
            'author_id': self.author.id,
            'category_id': self.category.id,
            'publisher_id': self.publisher.id,
            'price': '15000.00',
            'pages': 200,
            'isbn': '9780000000001',
            'publish_year': 2024,
            'stock': 5,
        }
        res = self.client.post('/api/v1/books/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_book_invalid_isbn(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test',
            'description': 'Test',
            'author_id': self.author.id,
            'category_id': self.category.id,
            'publisher_id': self.publisher.id,
            'price': '10000.00',
            'pages': 100,
            'isbn': 'ABCDEFGHIJKLM',  # xato ISBN
            'publish_year': 2024,
            'stock': 1,
        }
        res = self.client.post('/api/v1/books/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_ordering_by_price(self):
        res = self.client.get('/api/v1/books/?ordering=price')
        self.assertEqual(res.status_code, status.HTTP_200_OK)