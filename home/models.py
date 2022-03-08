from django.db import models
from datetime import datetime
# Create your models here.

class routine(models.Model):
    day = models.CharField(max_length=200)


# main models for storing workout details.
class set(models.Model):
    day = models.ForeignKey(routine,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # date = models.ForeignKey(date,on_delete=models.CASCADE)

class date(models.Model):
    date = models.DateField(auto_now=True)
#this is act as the category of the workout. For eg; Biceps, legs, butt, etc.

class workout(models.Model):
    name = models.CharField(max_length=200)
    set = models.ForeignKey(set,on_delete=models.CASCADE)
    # date = models.ForeignKey(date,on_delete=models.CASCADE)
#this will be the actual workout object. It will refrence to the workout by id.

class rep(models.Model):
    workout = models.ForeignKey(workout,on_delete=models.CASCADE)
    reps = models.CharField(max_length=120)
#now this will be the no of reps done on each day. this will refrence to the workout we did
# plus the date we performed it on and that workout object will refrence to the set.

class data(models.Model):
    day = models.ForeignKey(date,on_delete=models.CASCADE)
    set = models.ForeignKey(set,on_delete=models.CASCADE)

class transformation(models.Model):
    day = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='transformation')


#sub classes of workout
class instruction(models.Model):
    workout = models.ForeignKey(workout,on_delete=models.CASCADE)
    instruction = models.TextField()


class images(models.Model):
    workout = models.ForeignKey(workout,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
#################################
