from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('<int:bookId>', views.viewbook) #add only this line of code
]