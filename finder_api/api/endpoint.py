


from django.shortcuts import redirect

from finder_api.models import User


def add_to_favorites(request):
    user: User = request.user
    if user.is_authenticated:
        user.favorites.add(request.GET['id'])
        user.save()
    return redirect(f"{request.GET['loc']}")