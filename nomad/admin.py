from django.contrib import admin
from .models import Cafe, Member, Rating, Tag


admin.site.register(Cafe)
admin.site.register(Member)
admin.site.register(Rating)
admin.site.register(Tag)