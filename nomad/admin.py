from django.contrib import admin
from .models import Cafe, User, Rating, Tag


admin.site.register(Cafe)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Tag)