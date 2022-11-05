from django.contrib import admin

# Register your models here.
from .models import Actor, Movie, Tableform

admin.site.register(Movie)
admin.site.register(Tableform)
admin.site.register(Actor)
