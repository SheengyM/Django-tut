from django.urls import path
from . import views

urlpatterns = [
    path('Members/', views.Members, name='Members'),
]
