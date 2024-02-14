from django.shortcuts import render, get_object_or_404
from django.views import generic

from coffee.models import Coffee


def index(request, language_code=None):
    recipes = Coffee.objects.all()
    all_recipes = Coffee.objects.count()

    context = {
        "recipes": recipes,
        "language_code": language_code,
        "all_recipes": all_recipes,
    }

    return render(request, "coffee/index.html", context=context)


class CoffeeListView(generic.ListView):
    model = Coffee
    context_object_name = "coffee_list"
    template_name = "coffee/coffee_list.html"
    paginate_by = 5


def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, "coffee/coffee_detail.html", {"coffee": coffee})
