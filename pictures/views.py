from email.mime import image
from multiprocessing import context
from signal import pthread_kill
from unicodedata import category
from django.shortcuts import render, redirect
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
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        print('data:', data)
        print('image:', image)

        if data['category'] != 'none': 
            category = Category.objects.get(id = data['category'])
        elif data ['category_new'] != '':
            category, created = Category.objects.get_or_create(name = data['category_new'])
        else:
            category = None
        
        picture = Picture.objects.create(
            category = category,
            description = data['description'],
            image = image,

            )

        return redirect('gallery')



    context = {'categories': categories}

    return render(request, 'pictures/add.html', context)

