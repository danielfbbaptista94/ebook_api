from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    bibliography = models.TextField()

    def __str__(self):
        return self.last_name + " " + self.first_name

# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=140)
    resume = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.title

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    review_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return str(self.rating)