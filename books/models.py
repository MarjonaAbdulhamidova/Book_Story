from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name="Category Name"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Author(models.Model):
    full_name = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name="Full Name"
    )

    biography = models.TextField(
        blank=True,
        verbose_name="Biography"
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Birth Date"
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Country"
    )

    photo = models.ImageField(
        upload_to="authors/",
        blank=True,
        null=True,
        verbose_name="Photo"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Publisher"
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Address"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Phone Number"
    )

    email = models.EmailField(
        blank=True,
        verbose_name="Email"
    )

    website = models.URLField(
        blank=True,
        verbose_name="Website"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Book Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Author"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="books",
        verbose_name="Category"
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        related_name="books",
        verbose_name="Publisher"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price"
    )

    pages = models.PositiveIntegerField(
        verbose_name="Pages"
    )

    language = models.CharField(
        max_length=50,
        default="Uzbek",
        verbose_name="Language"
    )

    isbn = models.CharField(
        max_length=13,
        unique=True,
        db_index=True,
        verbose_name="ISBN"
    )

    publish_year = models.PositiveIntegerField(
        verbose_name="Publish Year"
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="Stock"
    )

    max_readers = models.PositiveIntegerField(
        default=0,
        verbose_name="Maximum Readers"
    )

    cover_image = models.ImageField(
        upload_to="books/",
        blank=True,
        null=True,
        verbose_name="Cover Image"
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="Available"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title