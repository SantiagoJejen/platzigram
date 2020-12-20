"""Users Model"""

#Django 
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    """Profile model. 
    proxy model that extends the base data whit other information """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length = 200, blank  = True )
    biography= models.TextField(blank = True, max_length = 200)
    phone_number = models.CharField(max_length =  20 , blank = True)
    picture = models.ImageField(upload_to='user/pictures', 
                                null = True,
                                blank = True)

    created = models.DateTimeField(auto_now_add =True)
    modified = models.DateTimeField(auto_now =True)

    def __str__(self):
        """Return User name"""
        return self.user.username