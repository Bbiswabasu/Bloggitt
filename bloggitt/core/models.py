from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
CATEGORY_CHOICES = ( 
    ("1", "Programming/Technology"), 
    ("2", "Health/Fitness"), 
    ("3", "Personal"), 
    ("4", "Fashion"), 
    ("5", "Food"), 
    ("6", "Travel"), 
    ("7", "Business"), 
    ("8", "Art"),
    ("9", "Other"), 
)  

class Post(models.Model):
    
    category = models.CharField( 
        max_length = 20, 
        choices = CATEGORY_CHOICES, 
        default = '1'
        ) 
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)



class FavouritePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)