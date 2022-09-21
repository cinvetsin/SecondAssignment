from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_mywatchlist(request):
    data_watchlist_item = MyWatchList.objects.all()
    var_have_watched = 0
    var_not_watched = 0
    for films in data_watchlist_item:
        if films.watched == "Sudah":
            var_have_watched += 1
        else:
            var_not_watched += 1
    notif = ""
    if(var_have_watched < var_not_watched):
        notif = "Wah, kamu masih sedikit menonton!"
    else:
        notif = "Selamat, kamu sudah banyak menonton!"
    context = {
        'list_movies': data_watchlist_item,
        'nama': 'Sasha Nabila Fortuna',
        'npm': '2106632226',
        'pesan' : notif
    }
    return render(request, "mywatchlist.html", context)

def send_watchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def send_watchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")