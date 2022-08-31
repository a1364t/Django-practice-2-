from django.contrib import admin
#from locallib import models 
from . import models


class BooksInstanceInline(admin.StackedInline):  #TabularInline
    model = models.BookInstance
    extra = 1


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]
  

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('title', 'author', 'genre')
    inlines = [BooksInstanceInline]

@admin.register(models.BookInstance)
class AdminBookInstance(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass



