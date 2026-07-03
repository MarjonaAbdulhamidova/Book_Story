import django
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from books.models import Category, Author, Publisher, Book

a1 = Author.objects.create(full_name="Abdulla Qodiriy", biography="O'zbek adabiyotining asoschisi", birth_date="1894-04-10", country="Uzbekistan")
a2 = Author.objects.create(full_name="Cho'lpon", biography="O'zbek shoiri va yozuvchisi", birth_date="1897-03-26", country="Uzbekistan")
a3 = Author.objects.create(full_name="Jules Verne", biography="Frantsuz fantastika yozuvchisi", birth_date="1828-02-08", country="France")
a4 = Author.objects.create(full_name="Arthur Conan Doyle", biography="Sherlock Holmes yaratuvchisi", birth_date="1859-05-22", country="UK")
a5 = Author.objects.create(full_name="G'afur G'ulom", biography="O'zbek shoiri", birth_date="1903-09-10", country="Uzbekistan")

p1 = Publisher.objects.create(name="Sharq nashriyoti", address="Toshkent", phone="+998712000000", email="info@sharq.uz", website="https://sharq.uz")
p2 = Publisher.objects.create(name="O'qituvchi", address="Toshkent", phone="+998712000001", email="info@oquvchi.uz", website="https://oquvchi.uz")

novel = Category.objects.get(pk=3)
science = Category.objects.get(pk=2)

Book.objects.create(title="O'tgan kunlar", description="Otabek va Kumushning muhabbat qissasi.", author=a1, category=novel, publisher=p1, price=45000, pages=384, language="Uzbek", isbn="9789943280011", publish_year=1926, stock=15, max_readers=100)
Book.objects.create(title="Mehrobdan chayon", description="Anvar va Ra'noning fojiaviy muhabbat qissasi.", author=a1, category=novel, publisher=p1, price=38000, pages=312, language="Uzbek", isbn="9789943280012", publish_year=1929, stock=10, max_readers=80)
Book.objects.create(title="Kecha va kunduz", description="Cho'lponning mashhur romani.", author=a2, category=novel, publisher=p1, price=42000, pages=296, language="Uzbek", isbn="9789943280013", publish_year=1936, stock=8, max_readers=60)
Book.objects.create(title="Yer ostida 20000 mil", description="Kapitan Nemo va Nautilus suv osti kemasi.", author=a3, category=science, publisher=p2, price=55000, pages=448, language="Uzbek", isbn="9789943280014", publish_year=1870, stock=20, max_readers=150)
Book.objects.create(title="Dunyoning 80 kunda aylanishi", description="Fileas Fogg 80 kunda dunyo bo'ylab sayohat.", author=a3, category=science, publisher=p2, price=48000, pages=320, language="Uzbek", isbn="9789943280015", publish_year=1872, stock=12, max_readers=120)
Book.objects.create(title="Sherlock Holmes sarguzashtlari", description="Buyuk detektiv Sherlock Holmes sarguzashtlari.", author=a4, category=novel, publisher=p2, price=62000, pages=512, language="Uzbek", isbn="9789943280016", publish_year=1892, stock=18, max_readers=200)
Book.objects.create(title="Shum bola", description="G'afur G'ulomning kulgili hikoyalar to'plami.", author=a5, category=novel, publisher=p1, price=32000, pages=224, language="Uzbek", isbn="9789943280017", publish_year=1936, stock=25, max_readers=180)
Book.objects.create(title="Yodgor", description="G'afur G'ulomning she'riy asari.", author=a5, category=novel, publisher=p1, price=28000, pages=180, language="Uzbek", isbn="9789943280018", publish_year=1944, stock=0, max_readers=50, is_available=False)
Book.objects.create(title="Ikki oy orasida", description="Oy sayyorasiga sayohat haqida roman.", author=a3, category=science, publisher=p2, price=51000, pages=360, language="Uzbek", isbn="9789943280019", publish_year=1865, stock=7, max_readers=90)
Book.objects.create(title="Baskervil iti", description="Sherlock Holmesning eng mashhur siri.", author=a4, category=novel, publisher=p2, price=44000, pages=256, language="Uzbek", isbn="9789943280020", publish_year=1902, stock=14, max_readers=110)

print(f"✅ Kitoblar: {Book.objects.count()} ta")
print(f"✅ Mualliflar: {Author.objects.count()} ta")
print(f"✅ Nashriyotlar: {Publisher.objects.count()} ta")