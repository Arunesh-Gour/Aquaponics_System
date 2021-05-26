from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
   # path('index/', views.index, name='index'),
   path('', views.index, name='index'),
   path('home/', views.home, name='home'),
   path('userlogin/', views.userlogin, name='login'),
   path('userlogout/', views.userlogout, name='logout'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('fetchdata/', views.fetchdata, name='fetchdata'),
]
