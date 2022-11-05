from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("newmovies/",views.new_release,name="newmovies"),
    path("actors/",views.actors,name="actors")


]
