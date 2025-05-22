from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)


class Posts(models.Model):
    image = models.ImageField(upload_to="posts/images")
    title = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag,related_name='tagged_posts')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
 

class Comments(models.Model):
    user_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    body = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")




