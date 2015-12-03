from django.forms import ModelForm
from predictions.models import Movie


class MovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ( 'description','user_ratings',)

