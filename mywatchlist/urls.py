# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_mywatchlist, send_watchlist_xml, send_watchlist_json, show_json_by_id, show_xml_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', send_watchlist_xml, name='send_watchlist_xml'),
    path('json/', send_watchlist_json, name='send_watchlist_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]