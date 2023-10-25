from django.db import models

# Create your models here.

#innharate Post with Model Super class
#post its model (subclass)
#sub class of model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True ) #dont axceed 256 length !! 
    #django give you PK named ID
    slug = models.SlugField(max_length=200, unique=True )
    body = models.TextField()
    created_on = models.DateTimeFieldField(auto_now_add=True )
    updated_on = models.DateTimeFieldField(auto_now=True )
    status = models.IntegerField(default=0)
