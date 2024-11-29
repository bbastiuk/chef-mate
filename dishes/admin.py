from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook, Dish, DishType

admin.site.register(Cook)
admin.site.register(Dish)
admin.site.register(DishType)