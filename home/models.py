from django.db import models

# Create your models here.

class Portfolio(models.Model):
    ad=models.CharField(max_length=50)
    soyad=models.CharField(max_length=50)
    ataadi=models.CharField(max_length=50)
    yas=models.IntegerField()
    tel=models.IntegerField()
    email=models.CharField(max_length=50)
    unvan=models.CharField(max_length=150)
    tehsil=models.CharField(max_length=50)
    isyeri=models.CharField(max_length=50)
    vezife=models.CharField(max_length=50)

    def __str__(self):
        return self.ad
