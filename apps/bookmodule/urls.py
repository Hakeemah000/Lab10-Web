from django.urls import path
from . import views

urlpatterns = [
 path('', views.index),
 path('index2/<int:val1>/', views.index2),
 path('<int:bookId>', views.viewbook),
 path('links.html', views.links, name='links'),
 path('formatting.html', views.formatting, name='formatting'),
 path('listing.html', views.listing, name='listing'),
 path('tables.html', views.tables, name='tables')

]
