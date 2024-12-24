from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView

from finder_api.models import Cuisine, Restaurant


class RestaurantListView(ListView):
    paginate_by = 2
    model = Restaurant


def index(request:HttpRequest) -> HttpResponse:
    res = Restaurant.objects.all()
    paginator = Paginator(res, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "app/index.html",
        {
            "page_obj": page_obj,
        }
    )
    
def cuisine(request:HttpRequest, catagory:str):
    cat = get_object_or_404(Cuisine, name=catagory)
    res = get_list_or_404(cat.restaurant_set)
    paginator = Paginator(res, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "app/cuisine.html",
        {
            "page_obj": page_obj,
            "name":cat.name, 
            "description":cat.description
        },
    )
    
def restaurant(request:HttpRequest, name:str):
    res = get_object_or_404(Restaurant,pk=name)
    return render(
        request,
        "app/restaurant.html",
        {"restaurant":res}
    )