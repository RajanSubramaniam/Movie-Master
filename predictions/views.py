from django.shortcuts import render
from predictions.models import Movie

# Create your views here.
def home(request):
	movies = Movie.objects.filter(user_ratings=5)

	return render(request, 'home.html',{
		'movies':movies,
	})








