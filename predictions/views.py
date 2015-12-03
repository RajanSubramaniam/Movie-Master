from django.shortcuts import render
from predictions.models import Movie

# Create your views here.
def home(request):
	movies = Movie.objects.filter(user_ratings=5)

	return render(request, 'home.html',{
		'movies':movies,
	})


def movie_detail(request, slug):
	movie=Movie.objects.get(slug=slug)
	
	return render(request, 'movies/movie_detail.html',{
		'movie':movie,
	})


def user(request):
	movies = Movie.objects.filter(user_ratings=5)

	return render(request, 'user.html',{
			'movies':movies,
	})













