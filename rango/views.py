from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    # Query the database for a list of all categories currently stored
    # Order the categories by the number of likes in descending order
    # retrieve the top 5 only 
    category_list = Category.objects.order_by('-likes')[:5]
    
    # Query the database for a list of all pages currently stored
    # Order the pages by the number of views in descending order
    # retrieve the top 5 only 
    page_list = Page.objects.order_by('-views')[:5]
    
    # place the list in our context_dict dictionary
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    
    #render the response and send it back
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Joel'}
    return render(request, 'rango/about.html', context=context_dict)
    
def show_category(request, category_name_slug):
    # create a context dictionary which we can pass to the tmeplate rendering engine 
    context_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
        
    return render(request, 'rango/category.html', context=context_dict)
