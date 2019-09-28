from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

# Category of the products : eg - Electronics, Fashion, Sports
class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length = 100)
    parent_cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class FinalCategory(models.Model):
    name = models.CharField(max_length = 100)
    parent_cat = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

# The taken photo from webcam = PRODUCT
class Product(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(FinalCategory, on_delete=models.SET_NULL, null=True)

## ** ## ** TODO: Fill up upload_to which saves the taken photo onto the directory
    photo = models.FileField(upload_to = "ecommerce/img/")

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

# The identified item based on the PRODUCT photo == ITEM
class Item(models.Model):
    name = models.CharField(max_length = 100)
    discount = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(1.0)])            # No discount if value == 0 #changed from IntegerField to DecimalField with validators
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField() 
    soldUnits = models.IntegerField()
    

## ** ## ** ## TODO: Fill up the file path where the item photos are stored, match takes a regEx (eg: foo(a-zA-Z)*), recursive == TRUE checks the subdirectory
    photo = models.FilePathField(path="ecommerce/img/",match=r'pencil',recursive=False)

    prodInferred = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) # The taken photo on webcam which infers to this item
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


# The customer of SHOPEE
class Customer(models.Model):
    name = models.CharField(max_length = 100)
        
    def __str__(self):
        return self.name

# The Order of an Item bought by a customer of SHOPEE (Order:Item is a M:N realtionship)
class Order(models.Model):
    order_id = models.IntegerField()
        
    def __str__(self):
        return self.order_id

# The bridge table between Order and Item
class Order_Item(order.Model):
    item = models.ForeignKey(Item, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)