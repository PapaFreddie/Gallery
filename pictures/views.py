from multiprocessing import context
from signal import pthread_kill
from django.shortcuts import render
from .models import Category, Picture

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    pictures = Picture.objects.all()
    context = {'categories': categories, 'pictures': pictures}
    return render(request, 'pictures/gallery.html', context)


def viewPicture(request, pk):
    picture = Picture.objects.get(id=pk)
    return render(request, 'pictures/picture.html', {'picture':picture})


def addPicture(request):
    return render(request, 'pictures/add.html')

