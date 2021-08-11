# Django specific settings
import inspect
import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# Your application specific imports
from standalone.models import Movie


movies_df = pd.read_csv("movies.csv")
movie = Movie(imdb_id="test", genres="test test test",
              original_title="title", overview="overview", vote_average="0.5",
              poster_path="/test.jpg",
              watched=False)
movie.save()
assert Movie.objects.count() > 0
