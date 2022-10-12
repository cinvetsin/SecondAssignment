# TODO: Implement Routings Here
from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_list, get_todolist_json, add_todolist

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_list, name='create_list'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add_todolist, name='add_todolist'),
]