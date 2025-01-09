from django.shortcuts import render
from rest_framework import generics, status
from .models import Book, UserProfile, Transaction
from .serializers import BookSerializer, UserSerializer, UserProfileSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
#Book views  
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# User Views
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated] #authenticated can only access
    
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Transaction Views
class CheckoutBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        user = request.user
        book = Book.objects.get(id=book_id)

        if book.copies_available > 0:
            Transaction.objects.create(user=user, book=book)
            book.copies_available -= 1
            book.save()
            return Response({"message": "Book checked out successfully!"}, status=status.HTTP_200_OK)
        return Response({"error": "No copies available!"}, status=status.HTTP_400_BAD_REQUEST)

class ReturnBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, transaction_id):
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.return_date = timezone.now()
        transaction.save()

        book = transaction.book
        book.copies_available += 1
        book.save()

        return Response({"message": "Book returned successfully!"}, status=status.HTTP_200_OK)
    


