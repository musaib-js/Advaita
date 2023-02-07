from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=250)
    timeslot = models.DateTimeField()
    description  = models.TextField()
    thumbnail = models.FileField(upload_to='media')
    slug = models.CharField(max_length = 50)


    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length = 150)
    subject  = models.CharField(max_length = 200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Sponsorship(models.Model):
    email = models.EmailField(max_length = 200)
    company_name = models.CharField(max_length = 200)
    contact_person = models.CharField(max_length = 200)
    designation = models.CharField(max_length = 200)
    mail = models.EmailField(max_length = 200)
    sponsorship_type = models.CharField(max_length = 200)

    def __str__(self):
        return self.company_name
    
class Sponsor(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length = 300)
    thumbnail = models.FileField(upload_to='media')

    def __str__(self):
        return self.name
    