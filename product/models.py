from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price=models.FloatField(default=0)
    courier_charges_maharashtra=models.FloatField(default=0)
    courier_charges_other_states=models.FloatField(default=0)
    discription=RichTextField(null=True,blank=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)
    image_1= models.ImageField(upload_to="images",default="",null=True)
    image_2= models.ImageField(upload_to="images",default="",null=True,blank=True)
    image_3= models.ImageField(upload_to="images",default="",null=True,blank=True)
    image_4= models.ImageField(upload_to="images",default="",null=True,blank=True)

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        image_1 = Image.open(self.image_1.path)
        output_size = (300,300)
        image_1.thumbnail(output_size)
        image_1.save(self.image_1.path)

        image_2 = Image.open(self.image_2.path)
        output_size = (300,300)
        image_2.thumbnail(output_size)
        image_2.save(self.image_2.path)

        image_3 = Image.open(self.image_3.path)
        output_size = (300,300)
        image_3.thumbnail(output_size)
        image_3.save(self.image_3.path)

        image_4 = Image.open(self.image_4.path)
        output_size = (300,300)
        image_4.thumbnail(output_size)
        image_4.save(self.image_4.path)



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)

class Select_category(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)