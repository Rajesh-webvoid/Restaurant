# from django.db import models
# import uuid

# class Restaurant(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     mobile_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = "Restaurant"
#         verbose_name_plural = "Restaurants"

#     def __str__(self):
#         return f"{self.name} - {self.address}"

# class RestaurantImage(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='restaurant_images/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Image for {self.restaurant.name}"

# class Menu(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
#     item_name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     RATING_CHOICES = [
#         (1, '1 Star'),
#         (2, '2 Stars'),
#         (3, '3 Stars'),
#         (4, '4 Stars'),
#         (5, '5 Stars'),
#     ]
#     rating = models.IntegerField(choices=RATING_CHOICES)
#     main_ingredients = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = "Menu"
#         verbose_name_plural = "Menus"

#     def __str__(self):
#         return f"{self.item_name} - {self.restaurant.name}"

# class MenuImage(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='menu_images/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Image for {self.menu.item_name}"

# class Review(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     RATING_CHOICES = [
#         (1, '1 Star'),
#         (2, '2 Stars'),
#         (3, '3 Stars'),
#         (4, '4 Stars'),
#         (5, '5 Stars'),
#     ]
#     review_rating = models.IntegerField(choices=RATING_CHOICES, default=3)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='reviews')
#     comment = models.TextField()

#     class Meta:
#         verbose_name = "Review"
#         verbose_name_plural = "Reviews"
#         ordering = ['id']

#     def __str__(self):
#         return f"Review for {self.menu.item_name}"

from django.db import models
import uuid

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return f"{self.name} - {self.address}"

class RestaurantImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='restaurant_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.restaurant.name}"

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)
    main_ingredients = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return f"{self.item_name} - {self.restaurant.name}"

class MenuImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='menu_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.menu.item_name}"

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    review_rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['id']

    def __str__(self):
        return f"Review for {self.menu.item_name}"
