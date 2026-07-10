from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Author, Publisher, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "book_count", "created_at")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("created_at", "updated_at")

    @admin.display(description="Kitoblar soni")
    def book_count(self, obj):
        count = obj.books.count()
        return format_html('<b style="color:#1a73e8">{}</b>', count)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "photo_preview", "full_name", "country", "birth_date", "book_count")
    search_fields = ("full_name", "country")
    list_filter = ("country",)
    ordering = ("full_name",)
    readonly_fields = ("photo_preview", "created_at", "updated_at")

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("full_name", "biography", "photo", "photo_preview")
        }),
        ("Qo'shimcha", {
            "fields": ("birth_date", "country", "created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    @admin.display(description="Rasm")
    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="height:50px;width:50px;border-radius:50%;object-fit:cover;" />',
                obj.photo.url
            )
        return "—"

    @admin.display(description="Kitoblar")
    def book_count(self, obj):
        return obj.books.count()


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email", "book_count")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Nashriyot ma'lumotlari", {
            "fields": ("name", "address", "phone", "email", "website")
        }),
        ("Tizim", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    @admin.display(description="Kitoblar")
    def book_count(self, obj):
        return obj.books.count()


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id", "cover_preview", "title", "author", "category",
        "price_display", "stock_display", "publish_year", "is_available",
    )

    list_filter = (
        "category", "language", "publisher",
        "publish_year", "is_available",
    )

    search_fields = (
        "title", "author__full_name",
        "publisher__name", "isbn",
    )

    list_editable = ("is_available",)
    list_per_page = 15
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("cover_preview", "created_at", "updated_at")
    autocomplete_fields = ["author", "publisher", "category"]

    # --- 🛠 ETISHMAYOTGAN FUNKSIYALAR SHU YERDA QO'SHILDI: ---

    @admin.display(description="Muqova")
    def cover_preview(self, obj):
        # Agar modelda rasm maydoni nomi 'cover' emas, 'cover_image' bo'lsa obj.cover_image deb o'zgartiring
        if hasattr(obj, 'cover') and obj.cover:
            return format_html(
                '<img src="{}" style="height:60px; width:45px; object-fit:cover; border-radius:4px; box-shadow: 0 2px 4px rgba(0,0,0,0.15);" />',
                obj.cover.url
            )
        elif hasattr(obj, 'cover_image') and obj.cover_image:
            return format_html(
                '<img src="{}" style="height:60px; width:45px; object-fit:cover; border-radius:4px; box-shadow: 0 2px 4px rgba(0,0,0,0.15);" />',
                obj.cover_image.url
            )
        return "—"

    @admin.display(description="Narxi")
    def price_display(self, obj):
        if hasattr(obj, 'price') and obj.price:
            return f"{obj.price:,} so'm".replace(",", " ")
        return "Bepul"

    @admin.display(description="Omborda")
    def stock_display(self, obj):
        if hasattr(obj, 'stock'):
            if obj.stock and obj.stock > 0:
                return format_html('<span style="color: #2e7d32; font-weight: bold;">{} ta bor</span>', obj.stock)
            return format_html('<span style="color: #c62828; font-weight: bold;">Tugagan</span>')
        return "—"