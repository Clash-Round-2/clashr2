from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
    questions=models.TextField()


class UserProfileInfo(models.Model):


    user = models.OneToOneField(User,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)
    quest1test = models.IntegerField(default=0)
    quest2test = models.IntegerField(default=0)
    quest3test = models.IntegerField(default=0)
    quest4test = models.IntegerField(default=0)
    quest5test = models.IntegerField(default=0)
    quest6test = models.IntegerField(default=0)
    totaltest=models.IntegerField(default=0)






    def __str__(self):

        return self.user.username
