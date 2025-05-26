from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tb_login(models.Model):
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    class meta:
        tb_table="tb_login"
        
class blah(models.Model):
    product_name=models.CharField(max_length=25)
    category=models.CharField(max_length=50, choices=[
        ('electronics','Electronics'),
        ('fashion','Fashion'),
        ('home_appliance','HomeAppliances'),
        ('books','Books'),
        ('jewellery','Jewellery')
    
    ])
    image_url=models.ImageField(upload_to="static/image/",null=True,blank=True)
    price=models.CharField(max_length=20)
    quantity=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    class meta:
        db_table="blah"
        
        
    def __str__ (self):
        return(self.product_name)


