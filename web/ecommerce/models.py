from django.db import models

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

# The taken photo from webcam = PRODUCT
class Product(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

## ** ## ** TODO: Fill up upload_to which saves the taken photo onto the directory
    photo = models.FileField(upload_to = "")

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

# The identified item based on the PRODUCT photo == ITEM
class Item(models.Model):
    name = models.CharField(max_length = 100)
    discount = models.IntegerField()            # No discount if value == 0
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField() 
    soldUnits = models.IntegerField()

## ** ## ** ## TODO: Fill up the file path where the item photos are stored, match takes a regEx (eg: foo(a-zA-Z)*), recursive == TRUE checks the subdirectory
    photo = models.FilePathField(path="",match="",recursive=)

    prodInferred = models.ForeignKey(Product, on_delete=models.CASCADE) # The taken photo on webcam which infers to this item
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name