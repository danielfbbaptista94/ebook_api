from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from ebooks.models import Author, Ebook, Review
from ebooks.api.serializers import AuthorSerializer, EbookSerializer, ReviewSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from ebooks.api.pagination import SmallSetPagination

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by("-id")
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class EBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

class EBookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by("-id")
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = SmallSetPagination

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)

        if review_queryset.exists():
            raise ValidationError("You already have a reviews of this book !")
        
        serializer.save(ebook=ebook, review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]