from django.contrib import admin
from predictions.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
	model = Movie
	list_display = ('title','genre','description','user_ratings',)
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Movie, MovieAdmin)



