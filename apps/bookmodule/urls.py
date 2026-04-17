from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.lab5_links, name="lab5_links"),
    path('html5/text/formatting/', views.lab5_formatting, name="lab5_formatting"),
    path('html5/listing/', views.lab5_listing, name="lab5_listing"),
    path('html5/tables/', views.lab5_tables, name="lab5_tables"),
    path('search/', views.search, name="books.search"),
    path('insert/', views.insert_books, name="books.insert"),
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
]
