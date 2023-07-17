from django.contrib import admin
from .models import Menu
from .models import CustomUser
from .models import Comment
from .models import Rezervation
from .models import Cart
from .models import Table

# Register your models here.,

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'is_published')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',) 
    list_search = ('name', 'category')
    list_per_page = 10

admin.site.register(Menu, MenuAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email')
    list_display_links = ('id', 'name', 'surname')
    list_search = ('name', 'surname', 'email')
    list_per_page = 10
admin.site.register(Comment, CommentAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display = ('tableNumber', 'is_published')
    
admin.site.register(Table, TableAdmin)

class RezervationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'date', 'time')
    list_display_links = ('id', 'name', 'surname')
    list_search = ('name', 'surname', 'email')
    list_per_page = 10
admin.site.register(Rezervation, RezervationAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'menu', 'quantity', 'price')
    list_display_links = ('id', 'user', 'menu')
    list_search = ('user', 'menu')
    list_per_page = 10
admin.site.register(Cart, CartAdmin)

