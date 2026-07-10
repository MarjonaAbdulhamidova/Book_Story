# 📚 Book Story API

Django REST Framework asosida qurilgan kitoblar kutubxonasi API.

## O'rnatish

```bash
git clone https://github.com/MarjonaAbdulhamidova/Book_Story.git
cd Book_Story/ecommerce-api
pip install -r requirements.txt
```

## Ishga tushirish

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Endpointlar

| Method | URL | Tavsif |
|--------|-----|--------|
| GET | /api/v1/books/ | Kitoblar ro'yxati |
| POST | /api/v1/books/ | Kitob qo'shish |
| GET | /api/v1/books/{id}/ | Kitob detail |
| PUT | /api/v1/books/{id}/ | Kitob yangilash |
| DELETE | /api/v1/books/{id}/ | Kitob o'chirish |
| GET | /api/v1/authors/ | Mualliflar |
| GET | /api/v1/categories/ | Kategoriyalar |
| GET | /api/v1/publishers/ | Nashriyotlar |

## Filter & Search