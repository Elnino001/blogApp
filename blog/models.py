from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('detail', args = [str(self.id)])


    def __str__(self):
        return self.title

class Comments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', args = [str(self.id)])
 
    

