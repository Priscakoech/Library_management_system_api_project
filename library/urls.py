from django.urls import path
from .views import BookListView, UserListView

urlpatterns = [
    path('api/books/', BookListView.as_view(), name='book-list'),
    path('api/users/', UserListView.as_view(), name='user-list'),
]