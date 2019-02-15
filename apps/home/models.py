from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.title



class MediaFiles(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/')
