from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
import pytz


class Account(models.Model):
    firstname = models.CharField(max_length = 30 , default='anonymous')
    lastname = models.CharField(max_length = 30 , default='anonymous')
    email = models.EmailField(default='elon@gmail.com')
    phone = models.CharField(max_length = 11)
    password = models.CharField(max_length = 50)
    profile_pic = models.FileField(default='anon.png')
    rating = models.IntegerField(default = 0)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
         return self.email



class Category(models.Model):
    category = models.CharField( max_length = 100 )

    def __str__(self):
         return self.category


class Talent(models.Model):
    category = models.ForeignKey(Category)
    talent = models.CharField( max_length = 100 )
    adjective = models.CharField( max_length = 100 , default="i can work")

    def __str__(self):
         return self.talent



class Employee(models.Model):
    account = models.ForeignKey(Account)
    is_active = models.BooleanField(default = True)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
         return self.account


class WhatDoYouDo(models.Model):
    employee = models.ForeignKey(Employee)
    talent = models.ForeignKey(Talent)

    def __str__(self):
         return self.talent

class WhatCanYouDo(models.Model):
    employee = models.ForeignKey(Employee)
    talent = models.ForeignKey(Talent)

    def __str__(self):
         return self.talent



class WhatHaveYouDone(models.Model):
    employee = models.ForeignKey(Employee)
    description = models.TextField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
         return self.description


class ImageReservoir(models.Model):
    whyd = models.ForeignKey(WhatHaveYouDone)
    image = models.FileField()

    def __str__(self):
         return self.image


class VideoReservoir(models.Model):
    whyd = models.ForeignKey(WhatHaveYouDone)
    video = models.FileField()

    def __str__(self):
         return self.video


class ForgotPassword(models.Model):
    email = models.EmailField()
    reset_code = models.CharField(default = '123579', max_length = 30)
    date = models.DateTimeField(default = timezone.now)




class RecentActivity(models.Model):
    account = models.ForeignKey(Account)
    employee = models.ForeignKey(Employee)
    date = models.DateTimeField(default = timezone.now) 

    def __str__(self):
        return 'recent'




class TopRated(models.Model):
    employee = models.ForeignKey(Employee)
    date = models.DateTimeField(default = timezone.now) 

    def __str__(self):
        return 'top rated'



class WhatsNew(models.Model):
    content_image = models.FileField()
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(default = timezone.now) 

    def __str__(self):
        return 'top rated'




class Chat(models.Model):
    account_1 = models.ForeignKey(Account)
    account_2 = models.IntegerField()
    delete_for_1 = models.BooleanField(default=False)
    delete_for_2 = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)


class Messenger(models.Model):
    chat = models.ForeignKey(Chat)
    messenger = models.ForeignKey(Account)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.message

    class Meta:
        ordering = ['date']



class Favorite(models.Model):
    account = models.ForeignKey(Account)
    favorite = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)



class RateReview(models.Model):
    account = models.ForeignKey(Account)
    client = models.IntegerField()
    rating = models.IntegerField()
    review = models.CharField(max_length= 150)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.review


class Appointment(models.Model):
    employer = models.ForeignKey(Account)
    employee = models.ForeignKey(Employee)
    date = models.DateTimeField(default = timezone.now)


class AppointmentDetail(models.Model):
    appointment = models.ForeignKey(Appointment)
    task = models.ForeignKey(Talent)
    description = models.TextField(default="description")
    appointment_date = models.CharField(default="1/8", max_length=20)
    appointment_time = models.CharField(default="12:00:00am", max_length=20)


class Status(models.Model):
    status = models.CharField(max_length=100)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):

        return self.status
    


class AppointmentStatus(models.Model):
    appointment = models.ForeignKey(Appointment)
    status = models.ForeignKey(Status)
    reason = models.CharField(max_length=200)
    date = models.DateTimeField(default = timezone.now)
