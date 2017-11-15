from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

class MemberSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'adress', 'phone_number', 'email', 'endofsubscription', 'image')

class BookSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'edition', 'release_date',
                  'number_of_page', 'langage', 'isnb', 'image', 'category')

class RentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = ('id', 'book', 'member', 'renting_date', 'returning_date', 'returned')

