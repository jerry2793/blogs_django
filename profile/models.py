from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="images/profile/",
        width_field=500,
        height_field=500
    )
    signiture = models.CharField(max_length=1000)
    theme = models.CharField(max_length=50,
        choices=(
            ('1','classic'),
            ('2','dark'),
            ('3','light')
        )
    )