from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')     # Show these columns in admin list
    search_fields = ('title', 'details') # Enable search bar for these fields
    list_filter = ('date',)              # Add filter by date

admin.site.register(Todo, TodoAdmin)
