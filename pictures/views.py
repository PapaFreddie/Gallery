from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'pictures/gallery.html')


def viewPicture(request, pk):
    return render(request, 'pictures/picture.html')


def addPicture(request):
    return render(request, 'pictures/add.html')

