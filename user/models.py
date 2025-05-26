from django.db import models 

# Create your models here.
class userlogin(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=25)
    password=models.CharField(max_length=25)
    confirmpassword=models.CharField(max_length=25)
    class meta:
        tb_table="userlogin"
class order(models.Model):
    productname=models.CharField(max_length=20)
    price=models.IntegerField(max_length=20)
    quantity=models.IntegerField(max_length=20)
    total=models.IntegerField(max_length=20)
    address=models.TextField(max_length=50)
    # image_url=models.ImageField(upload_to="static/image/",null=True,blank=True)
    class meta:
        tb_table="order"