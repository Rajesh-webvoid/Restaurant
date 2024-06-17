from django.contrib import admin
from .models import Restaurant, RestaurantImage, Menu, MenuImage, Review

class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 1  # Number of extra forms to display

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'mobile_number', 'email', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'address', 'email']
    inlines = [RestaurantImageInline]

class MenuImageInline(admin.TabularInline):
    model = MenuImage
    extra = 1  # Number of extra forms to display

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'restaurant', 'price', 'rating', 'created_at', 'updated_at']
    list_filter = ['rating', 'created_at', 'updated_at']
    search_fields = ['item_name', 'restaurant__name']
    inlines = [MenuImageInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['menu', 'review_rating', 'comment']
    list_filter = ['review_rating']
    search_fields = ['menu__item_name', 'comment']
