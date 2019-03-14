from django.db import models
from django.db.models import pre_save, post_save
# Create your models here.
class RestaurantLoction(models.Model):
    name         = models.CharField(max_length=120)
    location     = models.CharField(max_length=120,null=True,blank=True)
    category     = models.CharField(max_length=120,null=True,blank=True)
    timestamp    = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)
    slug         = models.SlugField(null=True, blank=True)
    #my_date_field  = models.DateTimeField(auto_now=False,auto_now_add=False)
    
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name
