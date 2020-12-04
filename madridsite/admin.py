from django.contrib import admin

from .models import Post,News,Like,Election,Comment

admin.site.register(Post)
admin.site.register(News)
admin.site.register(Like)
admin.site.register(Election)
admin.site.register(Comment)