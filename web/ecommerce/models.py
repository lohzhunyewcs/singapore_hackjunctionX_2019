from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import pandas as pd
import string
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

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
class Order_Item(models.Model):
    item = models.ForeignKey(Item, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)


def load_CatProd(cats123, prod_l):
    for k in range(len(cats123)):
        cats123[k] = list(cats123[k])
    for i in range(len(cats123[0])):
        cat_obj = Category(name=cats123[0][i])
        sub_cat_obj = SubCategory(name=cats123[1][i], parent_cat=cat_obj)
        final_cat_obj = SubCategory(name=cats123[2][i], parent_cat=sub_cat_obj)
        prod_obj = Product(name=prod_l[i], category=final_cat_obj)


    
# csv_file = "ecommerce/product_dataset.csv"
# df = pd.read_csv(csv_file)
# categories_l = df.product_category_tree
# prod_name_l = df.product_name

# prod_names = []
# cats123 = [set(),set(),set()]
# for i in range(len(categories_l)):
#     this_l = [ x.strip().translate(str.maketrans('','', string.punctuation)).lower() for x in categories_l[i].split(">>")]

#     if len(this_l) < 3:
#         break
#     if len(this_l) > 3:
#         this_l = this_l[(len(this_l)-3):]

#     for k in range(len(this_l)):
#         ind_cat = this_l[k]
#         cats123[k].add(ind_cat)

#     prod_names.append(prod_name_l[i])

# load_CatProd(cats123, prod_names)
