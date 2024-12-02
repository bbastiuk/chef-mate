from django.urls import path
from . import views

app_name = 'dishes'

urlpatterns = [
    path('', views.index, name='index'),
    path('dish-types/', views.DishTypeListView.as_view(), name='dish-type-list'),
    path('dishes/', views.DishListView.as_view(), name='dish-list'),
    path('cooks/', views.CookListView.as_view(), name='cook-list'),
]
