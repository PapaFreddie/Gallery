from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('picture/<int:pk>', views.viewPicture, name='picture'),
    path('add/', views.addPicture, name='add')
]
  

