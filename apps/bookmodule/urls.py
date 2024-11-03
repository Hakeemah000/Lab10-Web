# bookmodule/urls.py
from django.urls import path
from . import views

app_name = 'books'  # Add this line

urlpatterns = [
    path('', views.index, name="index"),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>/', views.viewbook),
    path('links.html', views.links, name='links'),
    path('formatting.html', views.formatting, name='formatting'),
    path('listing.html', views.listing, name='listing'),
    path('tables.html', views.tables, name='tables'),
    path('', views.index, name= "books.index"),
    path('list_books.html', views.list_books, name= "list_books"),
    path('one_book.html', views.one_book, name="view_one_book"),
    path('aboutus.html', views.aboutus, name="aboutus"),
    
]
