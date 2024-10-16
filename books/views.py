from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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
