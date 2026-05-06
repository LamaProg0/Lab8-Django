from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links_view, name='links'),
    path('html5/text/formatting', views.formatting_view, name='formatting'),
    path('html5/listing', views.listing_view, name='listing'),
    path('html5/tables', views.tables_view, name='tables'),
    path('search', views.search_view, name='books.search'),
    path('simple/query', views.simple_query),
    path('complex/query', views.complex_query),
    path('lab8/task1', views.task1_view, name='task1'),
    path('lab8/task2', views.task2_view, name='task2'),
    path('lab8/task3', views.task3_view, name='task3'),
    path('lab8/task4', views.task4_view, name='task4'),
    path('lab8/task5', views.task5_view, name='task5'),
    #path('lab8/task7', views.task7_view, name='task7'),
    path('lab9/task1', views.Lab9task1, name='lab9_task1'),
    path('lab9/task2', views.Lab9task2, name='lab9_task2'),
    path('lab9/task3', views.Lab9task3, name='lab9_task3'),
    path('lab9/task4', views.Lab9task4, name='lab9_task4'),
    path('lab9/task5', views.Lab9task5, name='lab9_task5'),
    path('lab9/task6', views.Lab9task6, name='lab9_task6'),
]

