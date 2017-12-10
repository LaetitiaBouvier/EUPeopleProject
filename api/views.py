from rest_framework.views import APIView

from .serializers import *
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import AUTH_USER_MODEL
from rest_framework.response import Response
from django.contrib.auth.models import User, AnonymousUser


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({ 'token': token.key, 'id': token.user_id })

# Create your views here.

class CurrentUserView(APIView):
    queryset = User.objects.all()
    serializers_class = MemberSerialiser

    def get(self, request):
        if type(request.user) != AnonymousUser :
            serializer = MemberSerialiser(request.user)
        else :
            return Response("Unauthentificated.", 503)
        return Response(serializer.data)

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        queryset = Author.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')

        if first_name:
            queryset = queryset.filter(first_name__contains=first_name)
        if last_name:
            queryset = queryset.filter(last_name__contains=last_name)

        return queryset

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerialiser

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerialiser

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser

class RentList(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerialiser

class RentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerialiser

