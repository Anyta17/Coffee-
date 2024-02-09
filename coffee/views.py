from django.shortcuts import render, get_object_or_404
from django.views import generic

from coffee.models import Coffee


def index(request):
    recipes = Coffee.objects.all()

    context = {
        "recipes": recipes,
    }

    return render(request, "coffee_app/index.html", context=context)


class CoffeeListView(generic.ListView):
    model = Coffee
    context_object_name = "coffee_list"
    template_name = "coffee_app/coffee_list.html"
    paginate_by = 5


def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, "coffee_app/coffee_detail.html", {"coffee": coffee})
