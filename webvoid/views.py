from django.shortcuts import render, get_object_or_404
from .models import Restaurant,Review,Menu

def restaurant_list(request):
    if request.method =="POST":
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
    restaurants = Restaurant.objects.all()


    return render(request, 'index.html', {'restaurants': restaurants})




def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurant_details.html', {'restaurant': restaurant})

# def menu_detail(request, menu_id):
#     menu = get_object_or_404(Menu, pk=menu_id)
#     reviews = Review.objects.filter(menu=menu)
#     return render(request, 'menu_detail.html', {'menu': menu, 'reviews': reviews})

from django.shortcuts import render, get_object_or_404
from .models import Menu

def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    reviews = menu.reviews.all()
    images = menu.images.all()
    return render(request, 'menu_detail.html', {'menu': menu, 'reviews': reviews, 'images': images})


