from django.urls import path
from .views import index, CoffeeListView, coffee_detail, switch_language

urlpatterns = [
    path("switch-language/<str:language_code>/", switch_language, name="switch-language"),
    path("<str:language_code>/", index, name="index"),
    path("<str:language_code>/coffee/", CoffeeListView.as_view(), name="coffee-list"),
    path("<str:language_code>/coffee/<int:pk>/", coffee_detail, name="coffee-detail"),
]

app_name = "coffee"
