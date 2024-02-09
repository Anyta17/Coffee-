from django.urls import path
from .views import index, CoffeeListView, coffee_detail

urlpatterns = [
    path("", index, name="index"),
    path("coffee/", CoffeeListView.as_view(), name="coffee-list"),
    path("coffee/<int:pk>/", coffee_detail, name="coffee-detail"),
]

app_name = "coffee"
