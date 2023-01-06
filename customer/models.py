from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.



class Country(models.Model):
    country = models.CharField(max_length=2, blank=False,null=False)
    Country_Description = models.CharField(max_length=80, blank=False,null=False)


    def __str__(self) -> str:
        return self.Country_Description 
    class Meta:
        db_table = 'Country'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(default=None)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True)
    address = models.CharField(max_length=255, default=None)
    profilePic = models.ImageField()

    def __str__(self):
        return self.user.username