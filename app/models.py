
from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_created = models.DateTimeField(auto_now=True)
    is_updated = models.DateTimeField(auto_now=True)

class User(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    question = models.TextField(max_length=500)
    option1 = models.CharField(max_length=50,default="0")
    option2 = models.CharField(max_length=50,default="0")
    option3 = models.CharField(max_length=50,default="0")
    option4 = models.CharField(max_length=50,default="0")

class Poll(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.TextField(max_length=500)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)
    option4_count = models.IntegerField(default=0)
    is_created = models.DateTimeField(auto_now=True)

    def total(self):
        return self.option1_count + self.option2_count + self.option3_count + self.option4_count