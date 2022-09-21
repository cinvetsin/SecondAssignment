from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_mywatchlist(request):
    data_watchlist_item = MyWatchList.objects.all()
    context = {
        'list_movies': data_watchlist_item,
        'nama': 'Sasha Nabila Fortuna',
        'npm': '2106632226'
    }
    return render(request, "mywatchlist.html", context)

def send_watchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def send_watchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")