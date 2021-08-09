from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'movierecommender'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.MovieListView.as_view(), name='index'),
]