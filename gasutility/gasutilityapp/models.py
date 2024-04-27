from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Connections(models.Model):
    GEN=(('Male','Male'),('Female','Female'))
    STATUS=(('Single','Single'),('Married','Married'),('Divorced','Divorced'),('Widowed','Widowed'))
    cname = models.CharField(max_length=100,verbose_name='Name')
    cemail = models.CharField(max_length=100,verbose_name='Email')
    cmobile = models.CharField(max_length=10,verbose_name='Mobile Number')
    cgender = models.CharField(max_length=10,verbose_name='Gender',choices=GEN)
    cstatus = models.CharField(max_length=10,verbose_name='Marrital Status',choices=STATUS)
    caadhar = models.CharField(max_length=12,verbose_name='Aadhar Card Number')
    caddress = models.CharField(max_length=300,verbose_name='Address')
    cpincode = models.IntegerField()
    cdob = models.DateField()
    cdate = models.DateTimeField(auto_now_add=True)


class BookingGass(models.Model):
    REF=(('5 - Rs.500','5 - Rs.500'),('10 - Rs.800','10 - Rs.800'),('15 - Rs.1000','15 - Rs.1000'),('20 - Rs.1500','20 - Rs.1500'),('25 - Rs.1800','25 - Rs.1800'),('30 - Rs.2000','30 - Rs.2000'))
    STATUS=(('Confirmed','Confirmed'),('On the Way','On the Way'),('Delivered','Delivered'))
    connection = models.ForeignKey(Connections, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='Name')
    email = models.CharField(max_length=100,verbose_name='Email')
    mobile = models.CharField(max_length=10,verbose_name='Mobile Number')
    address = models.CharField(max_length=300,verbose_name='Address')
    ref = models.CharField(max_length=20,verbose_name='Reffiling',choices=REF)
    status = models.CharField(max_length=15,verbose_name='Delivery Status',choices=STATUS,default='in progress')
    bookdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 