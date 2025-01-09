from django.urls import path
from .views import (
    BookListView, UserListView, BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    UserListCreateAPIView,
    CheckoutBookAPIView,
    ReturnBookAPIView,)
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='book-list'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('checkout/<int:book_id>/', CheckoutBookAPIView.as_view(), name='checkout-book'),
    path('return/<int:transaction_id>/', ReturnBookAPIView.as_view(), name='return-book'),
]