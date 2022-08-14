from django.shortcuts import render, redirect
from core.models import event
from feed.models import Category, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def gallery(request):

  
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'feed/gallery.html', context)



def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'feed/photo.html', {'photo': photo})



def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'feed/add.html', context)

def events(request):
    eventinng = event.objects.all()
    return render(request, 'event.html', {'event': eventinng})