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
    path('insert/more/', views.insert_more_books, name="books.insert_more"),
    path('lab8/task1/', views.lab8_task1, name="lab8_task1"),
    path('lab8/task2/', views.lab8_task2, name="lab8_task2"),
    path('lab8/task3/', views.lab8_task3, name="lab8_task3"),
    path('lab8/task4/', views.lab8_task4, name="lab8_task4"),
    path('lab8/task5/', views.lab8_task5, name="lab8_task5"),
    path('insert/students/', views.insert_students, name="insert_students"),
    path('lab8/task7/', views.lab8_task7, name="lab8_task7"),
]
