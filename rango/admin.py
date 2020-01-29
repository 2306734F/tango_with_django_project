from django.contrib import admin
from rango.models import Category, Page

#class PageInLine(admin.TabularInLine):
#    model = Page
#    extra = 3
    
class PageAdmin(admin.ModelAdmin):
    list_display  =  ('title','category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
