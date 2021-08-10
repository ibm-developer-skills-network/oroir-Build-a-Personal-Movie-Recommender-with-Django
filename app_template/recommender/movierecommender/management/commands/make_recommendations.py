from django.core.management import BaseCommand
from ...models import Movie


# Check if genres are valid
def check_valid_genres(genres: str):
    if bool(genres and not genres.isspace()) and genres != 'na':
        return True
    else:
        return False

# python manage.py make_recommendations
