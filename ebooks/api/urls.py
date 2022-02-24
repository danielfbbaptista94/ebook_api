from django.urls import path

from ebooks.api.views import (
    AuthorListCreateAPIView, AuthorDetailAPIView, 
    EBookListCreateAPIView, EBookDetailAPIView,
    ReviewListCreateAPIView, ReviewDetailAPIView
)


urlpatterns = [
    path(
        "authors/",
        AuthorListCreateAPIView.as_view(),
        name="authors-list"
    ),
    path(
        "authors/<int:pk>/",
        AuthorDetailAPIView.as_view(),
        name="authors-detail"
    ),
    path(
        "ebooks/",
        EBookListCreateAPIView.as_view(),
        name="ebooks-list"
    ),
    path(
        "ebooks/<int:pk>/",
        EBookDetailAPIView.as_view(),
        name="ebooks-detail"
    ),
    path(
        "ebooks/<int:ebook_pk>/reviews/",
        ReviewListCreateAPIView.as_view(),
        name="reviews-list"
    ),
    path(
        "reviews/<int:pk>/",
        ReviewDetailAPIView.as_view(),
        name="reviews-detail"
    ),
]