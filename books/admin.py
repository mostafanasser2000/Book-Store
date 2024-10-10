from django.contrib import admin
from .models import Book


class BookModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "price"]
    list_filter = ["author"]
    search_fields = ["title"]


admin.site.register(Book, BookModelAdmin)
