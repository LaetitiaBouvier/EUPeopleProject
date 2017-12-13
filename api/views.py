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

    def get_queryset(self):
        queryset = Member.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        adress = self.request.query_params.get('adress')
        phone = self.request.query_params.get('phone')
        email = self.request.query_params.get('email')
        endofsubscription = self.request.query_params.get('endofsubscription')

        if first_name:
            queryset = queryset.filter(first_name__contains=first_name)
        if last_name:
            queryset = queryset.filter(last_name__contains=last_name)
        if adress:
            queryset = queryset.filter(adress__contains=adress)
        if phone:
            queryset = queryset.filter(phone__contains=phone)
        if email:
            queryset = queryset.filter(email=last_name)
        if endofsubscription:
            queryset = queryset.filter(last_name__contains=last_name)

        return queryset

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerialiser

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser

    def get_queryset(self):
        queryset = Author.objects.all()
        author = self.request.query_params.get('author')
        title = self.request.query_params.get('title')
        edition = self.request.query_params.get('edition')
        release_date = self.request.query_params.get('release_date')
        number_of_pages = self.request.query_params.get('number_of_pages')
        langage = self.request.query_params.get('langage')
        isnb = self.request.query_params.get('isnb')
        category = self.request.query_params.get('category')

        if author:
            queryset = queryset.filter(first_name__contains=author)
        if title:
            queryset = queryset.filter(last_name__contains=title)
        if edition:
            queryset = queryset.filter(edition__contains=edition)
        if release_date:
            queryset = queryset.filter(release_date__contains=release_date)
        if number_of_pages:
            queryset = queryset.filter(number_of_pages__contains=number_of_pages)
        if langage:
            queryset = queryset.filter(langage__contains=langage)
        if isnb:
            queryset = queryset.filter(isnb__contains=isnb)
        if category:
            queryset = queryset.filter(category__contains=category)

        return queryset

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser

class RentList(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerialiser

    def get_queryset(self):
        queryset = Author.objects.all()
        book = self.request.query_params.get('book')
        member = self.request.query_params.get('member')
        renting_date = self.request.query_params.get('renting_date')
        returning_date = self.request.query_params.get('returning_date')
        returned = self.request.query_params.get('returned')

        if book:
            queryset = queryset.filter(book__contains=book)
        if member:
            queryset = queryset.filter(member__contains=member)
        if renting_date:
            queryset = queryset.filter(renting_date__contains=renting_date)
        if returning_date:
            queryset = queryset.filter(returning_date__contains=returning_date)
        if returned:
            queryset = queryset.filter(returned__contains=returned)


        return queryset

class RentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerialiser

