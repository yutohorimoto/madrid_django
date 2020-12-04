from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from mdeditor.fields import MDTextField 
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = MDTextField() 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class News(models.Model):
    news_title = models.TextField()
    news_url =  models.TextField()
    view_number = models.IntegerField(blank=False, default=0)
    like_number = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.news_title

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like_user')
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

class Election(models.Model):
    player = models.TextField()
    number = models.IntegerField(blank=False, default=0)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text