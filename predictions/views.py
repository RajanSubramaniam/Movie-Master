from django.shortcuts import render, redirect
from predictions.forms import MovieForm
from predictions.models import Movie
from django.template.defaultfilters import slugify

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


def edit_movie(request, slug):
	movie=Movie.objects.get(slug=slug)
	form_class = MovieForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=movie)
		if form.is_valid():
			form.save()
			return redirect('movie_detail', slug=movie.slug)
	else:
		form = form_class(instance=movie)

	return render(request,'movies/edit_movie.html',{
			'movie':movie,
			'form': form,
	})

def user(request):
	movies = Movie.objects.filter(user_ratings=5)

	return render(request, 'user.html',{
			'movies':movies,
	})




def create_movie(request):
	form_class = MovieForm
	if request.method == 'POST':
		form=form_class(request.POST)
		if form.is_valid():
			movie=form.save(commit=False)
			movie.user=request.user
			movie.slug=slugify(movie.title)
			movie.save()
			return redirect('movie_detail',slug=movie.slug)
	else:
		form=form_class()

	return render(request, 'movies/add_movie.html', {
			'form': form,
	})




def browse_by_name(request, initial=None):
	if initial:
		movies = Movie.objects.filter(
			title__istartswith=initial).order_by('title')
	else:
		movies = Movie.objects.all().order_by('title')
	return render(request,'search/search.html',{
		'movies':movies,
		'initial': initial,
	})






















