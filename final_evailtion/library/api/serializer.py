from rest_framework import serializer
from .models import Auther, Book, Country, BookCountry

class AuthorSerializer(serializer.ModelSerializer):
    class Meta:
        model = Author
        field = '__all__'

    class BookCountrySerializer(serializer.ModelSerializer):
        class Meta:
            model = BookCountry
            field = '__all__'
