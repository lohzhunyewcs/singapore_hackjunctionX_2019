from django.contrib import admin
from ecommerce.models import Category, SubCategory, FinalCategory, Product, Seller, Item, Customer, Order, Order_Item
# Register your models here.
# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(FinalCategory)
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Item)
admin.site.register(Order_Item)
admin.site.register(Order)
admin.site.register(Customer)