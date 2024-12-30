from datetime import datetime, UTC
import uuid
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest

from finder_api.models import Cuisine, Restaurant
from finder_api.models.user import User
from finder_api.forms import ReviewsForm



def index(request:HttpRequest) -> HttpResponse:
    res = Restaurant.objects.all()
    paginator = Paginator(res, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "app/index.html",
        {
            "page_obj": page_obj,
        }
    )



def about(request:HttpRequest) -> HttpResponse:
    return render(
        request,
        "app/about.html",
    )
    

def cuisine(request:HttpRequest, catagory:str):
    cat = get_object_or_404(Cuisine, name=catagory)
    res = cat.restaurant_set.all()
    paginator = Paginator(res, 10)
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


def all_cuisine(request:HttpRequest):
    cat = get_list_or_404(Cuisine)
    paginator = Paginator(cat, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(
        request,
        "app/cuisine_all.html",
        {
            "page_obj": page_obj,
        },
    )
    

def restaurant(request:HttpRequest, name:str):
    form = ReviewsForm(request.POST or None)
    res = get_object_or_404(Restaurant,pk=name)
    if form.is_valid():
        form_made = form.save(commit=False)
        form_made.created_by = request.user
        form_made.pub_date = datetime.now(tz=UTC)
        form_made.uuid = str(uuid.uuid4())
        form_made.save()
    return render(
        request,
        "app/restaurant.html",
        {
            "restaurant":res, 
            "form": form
        }
    )
    
    

def search(request:HttpRequest):
    query = request.GET.get("q")
    results = Restaurant.objects.filter(name__icontains=query) if query else Restaurant.objects.none()
    
    paginator = Paginator(results, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'app/search.html', context)

def account(request:HttpRequest):
    user = request.user
    results = user.favorites.all()
    
    paginator = Paginator(results, 2)
    page_number = request.GET.get('page_res')
    res_obj = paginator.get_page(page_number)
    
    results = user.reviews_set.all()
    
    paginator = Paginator(results, 2)
    page_number = request.GET.get('page_rev')
    rev_obj = paginator.get_page(page_number)
    
    return render(request, "app/account.html", {"res_obj":res_obj, "rev_obj":rev_obj})


def other_users(request:HttpRequest, uuid: str):
    user = User.objects.get(uuid=uuid)
    if user.is_public:
        results = user.favorites.all()
        
        paginator = Paginator(results, 2)
        page_number = request.GET.get('page_res')
        res_obj = paginator.get_page(page_number)
        
        results = user.reviews_set.all()
        
        paginator = Paginator(results, 2)
        page_number = request.GET.get('page_rev')
        rev_obj = paginator.get_page(page_number)
        
        return render(request, "app/account_public.html", {"user":{"is_public":True, "username":user.username},"res_obj":res_obj, "rev_obj":rev_obj})
    
    return render(request, "app/account_public.html", {"user":{"is_public":False, "username":user.username}})
    
def privacy(request:HttpRequest):
    return render(request, "app/privacy.html")

    
def tos(request:HttpRequest):
    return render(request, "app/tos.html")
