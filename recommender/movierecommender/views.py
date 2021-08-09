from django.shortcuts import render
import pandas as pd
from django.views import generic
from .models import Movie


# MovieListView
class MovieListView(generic.ListView):
    """Movie List generic view"""

    # HTML template name
    template_name = 'movierecommender/movie_list.html'
    # Context object for the template
    context_object_name = 'movie_list'

    def get_queryset(self):
        # Show only movies in recommendation list
        # Sorted by vote_average in desc

        # Get recommended movie counts
        recommended_count = Movie.objects.filter(
             recommended=True
        ).count()
        # If there are no recommended movies
        if recommended_count == 0:
            # Just return the top voted and unwatched movies as popular ones
            movies = Movie.objects.filter(
                 watched=False
            ).order_by('-vote_count')[:30]
            return movies
        else:
            # Get the top voted, unwatched, and recommended movies
            movies = Movie.objects.filter(
                watched=False
            ).filter(
                recommended=True
            ).order_by('-vote_count')[:50]
            return movies
