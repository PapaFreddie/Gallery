from multiprocessing import context
from django.shortcuts import render
from .models import Category, Picture

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'pictures/gallery.html', context)


def viewPicture(request, pk):
    return render(request, 'pictures/picture.html')


def addPicture(request):
    return render(request, 'pictures/add.html')

