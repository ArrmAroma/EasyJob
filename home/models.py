from django.db import models

# Create your models here.
class Entrepreneur(models.Model):
    compname                     = models.CharField(max_length=255)
    password                    = models.CharField(max_length=255)
    category                    = models.CharField(max_length=255)
    phone                       = models.CharField(max_length=255)
    email                       = models.CharField(max_length=255)
    address                     = models.CharField(max_length=255)
    description                 = models.CharField(max_length=255)

class Member(models.Model):
    name                    = models.CharField(max_length=255)
    name_eng                = models.CharField(max_length=255)
    birth_day               = models.CharField(max_length=255)
    sex                     = models.CharField(max_length=255)
    nationality             = models.CharField(max_length=255)
    religion                = models.CharField(max_length=255)
    phone                   = models.CharField(max_length=255)
    email                   = models.CharField(max_length=255)
    grade                   = models.CharField(max_length=255)
    school                  = models.CharField(max_length=255)
    faculty                 = models.CharField(max_length=255)
    major                   = models.CharField(max_length=255)
    education_category      = models.CharField(max_length=255)
    state                   = models.CharField(max_length=255)
    year                    = models.CharField(max_length=255)
    gpa                     =  models.CharField(max_length=255)
    application_form        = models.ForeignKey(Entrepreneur,on_delete=models.CASCADE)