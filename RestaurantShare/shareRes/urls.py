from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("restaurantDetail/delete", views.delete_restaurant, name="resDelete"),
    path("restaurantDetail/<str:res_id>", views.restaurantDetail, name="resDetailPage"),
    path(
        "restaurantDetail/updatePage/update", views.update_restaurant, name="resUpdate"
    ),
    path(
        "restaurantDetail/updatePage/<str:res_id>",
        views.restaurantUpdate,
        name="resUpdatePage",
    ),
    path("restaurantCreate/", views.restaurantCreate, name="resCreatePage"),
    path("restaurantCreate/create", views.create_restaurant, name="resCreate"),
    path("categoryCreate/", views.categoryCreate, name="cateCreatePage"),
    path("categoryCreate/create", views.create_category, name="cateCreate"),
    path("categoryCreate/delete", views.delete_category, name="cateDelete"),
]
