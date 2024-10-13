from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review


class BookModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "price"]
    list_filter = ["author"]
    search_fields = ["title"]
    inlines = [
        ReviewInline,
    ]


admin.site.register(Book, BookModelAdmin)
