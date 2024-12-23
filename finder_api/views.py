from django.shortcuts import get_object_or_404, render, get_list_or_404

from django.http import HttpResponse, HttpRequest

from finder_api.models import Cuisine, Restraunt


def index(request:HttpRequest) -> HttpResponse:
    res = get_list_or_404(Restraunt)
    all_gathered = [i.dict() for i in res]
    return render(
        request,
        "app/index.html",
        {
            "restaurants": all_gathered,
        }
    )
    
def cuisine(request:HttpRequest, catagory:str):
    cat = get_object_or_404(Cuisine, name=catagory)
    res = get_list_or_404(cat.restraunt_set)
    all_gathered = [i.dict() for i in res]
    return render(
        request,
        "app/cuisine.html",
        {
            "restaurants": all_gathered,
            "name":cat.name, 
            "description":cat.description
        },
    )