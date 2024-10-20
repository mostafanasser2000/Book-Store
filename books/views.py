from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    login_url = "account_login"
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = "account_login"
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    permission_required = ["books.special_status"]
    queryset = Book.objects.all().prefetch_related(
        "reviews__author",
    )


class SearchResultListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("q")

        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
