from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

class MemberSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Member
        fiels = ('id', 'first_nale', 'last_name', 'adress', 'phone_number', 'email', 'endofsubscription')