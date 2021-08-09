from django.shortcuts import render
import pandas as pd
from django.views import generic
from .models import Movie


# MovieListView
class MovieListView(generic.ListView):
    template_name = 'movierecommender/movie_list.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        # Show only movies in recommendation list
        # Sorted by vote_average in desc
        recommended_count = Movie.objects.filter(
             recommended=True
        ).count()
        if recommended_count == 0:
            courses = Movie.objects.filter(
                 watched=False
            ).order_by('-vote_count')[:30]
            return courses
        else:
            # Query the top recommended movie
            courses = Movie.objects.filter(
                watched=False
            ).filter(
                recommended=True
            ).order_by('-vote_count')[:50]
            return courses
