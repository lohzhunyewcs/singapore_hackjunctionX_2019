from django.contrib import admin
from ecommerce.models import Post, Category, SubCategory, FinalCategory, Product, Seller, Item
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(FinalCategory)
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Item)