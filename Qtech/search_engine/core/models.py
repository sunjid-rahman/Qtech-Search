from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    name=models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Result(models.Model):
    keyword=models.ForeignKey(Keyword,related_name='sharedKeyword',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='sharedUser',null=True,blank=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    description=models.TextField(blank=True,default='')
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.title
