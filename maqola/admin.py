from django.contrib import admin
from .models import Category, Comment, Like,Maqola
# Register your models here.

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Maqola)
