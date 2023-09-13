from django.contrib import admin
from .models import Author

# Register your models here.
class AuthorAdmin(Author):
    list_display = ("firstname", "lastname", "date",)
    
admin.site.register(Author)
