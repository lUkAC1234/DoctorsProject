from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# --------------------------------------------------------------------------- #
# Users
class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/profile/image/%Y/%m/%d/', default='naturepreloader.jpeg')
# --------------------------------------------------------------------------- #
    
    
class VideosModel(models.Model):
    name = models.CharField(max_length=100)
    preload_image = models.ImageField(upload_to='videos-media/preloadimages/%Y/%m/%d/')
    video = models.FileField(upload_to='videos-media/videos/%Y/%m/%d/')
    description = models.TextField()
    short_description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
class Commentsmodel(models.Model):
    post = models.ForeignKey(VideosModel, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=100)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text}"
    
    class Meta:
        ordering = ('-id',)