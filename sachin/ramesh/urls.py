from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home',views.home, name='home'),
    path('success',views.success, name='success'),
    path('failure',views.failure, name='failure')
]
