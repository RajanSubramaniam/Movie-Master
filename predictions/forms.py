from django.forms import ModelForm
from predictions.models import Movie


class MovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ( 'title','genre','description','user_ratings',)



