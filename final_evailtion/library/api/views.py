from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly,  IsAuthenticateed
from rest_framework.pagination import PageNumberPagination
from .models import Author, Book, Country, BookCountry
from .serializer import AuthorSerializer, BookSerializer, Countryserializer, BookCountrySerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
class AuthorViewSet(viewsets.ModelViewset):
    queryset = Author.object.all(
    serializer_class = AuthorSerilizer
    )
class CountryViewSet(viewsets.ModelViewset):
    queryset = Country.object.all(
    serializer_class = CountrySerilizer
    )
class BookViewSet(viewsets.ModelViewset):
    queryset = Book.object.all(
    serializer_class = BookSerilizer
    )


