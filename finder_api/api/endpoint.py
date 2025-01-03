from django.http import JsonResponse

from finder_api.models import User


def add_to_favorites(request):
    user: User = request.user
    if user.is_authenticated:
        ct = user.favorites.count()
        user.favorites.add(request.GET['id'])
        user.save()
    if ct == user.favorites.count():
        res = JsonResponse({"error":"No Content Changed"})
        res.status_code = 304
        return res
    res = JsonResponse({"reply":"Added to your favorites"})
    res.status_code = 200
    return res


def remove_to_favorites(request):
    user: User = request.user
    if user.is_authenticated:
        ct = user.favorites.count()
        user.favorites.remove(request.GET['id'])
        user.save()
    if ct == user.favorites.count():
        res = JsonResponse({"error":"No Content Changed"})
        res.status_code = 304
        return res
    res = JsonResponse({"reply":"Removed from your favorites"})
    res.status_code = 200
    return res


def add_to_following(request):
    user: User = request.user
    if user.is_authenticated:
        ct = user.favorites.count()
        user.favorites.remove(request.GET['id'])
        user.save()
    if ct == user.favorites.count():
        res = JsonResponse({"error":"No Content Changed"})
        res.status_code = 304
        return res
    res = JsonResponse({"reply":"Removed from your favorites"})
    res.status_code = 200
    return res



def remove_from_following(request):
    user: User = request.user
    if user.is_authenticated:
        ct = user.favorites.count()
        user.favorites.remove(request.GET['id'])
        user.save()
    if ct == user.favorites.count():
        res = JsonResponse({"error":"No Content Changed"})
        res.status_code = 304
        return res
    res = JsonResponse({"reply":"Removed from your favorites"})
    res.status_code = 200
    return res
