from django.contrib import admin

from users.models import User
from reviews.models import Genre, Title, Category, Comments, Review

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Review)
