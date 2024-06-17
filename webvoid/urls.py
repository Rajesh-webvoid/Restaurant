from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<uuid:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('menu/<uuid:menu_id>/', views.menu_detail, name='menu_detail'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


