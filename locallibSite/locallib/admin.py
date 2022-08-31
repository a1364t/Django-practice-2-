from django.contrib import admin
#from locallib import models 
from .models import Author, Genre, Book, BookInstance


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)

