import uuid
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.0)]
    )
    cover = models.ImageField(upload_to="covers/", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})


class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(), related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.review
