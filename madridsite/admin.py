from django.contrib import admin

from .models import Post,News,Like

admin.site.register(Post)
admin.site.register(News)
admin.site.register(Like)