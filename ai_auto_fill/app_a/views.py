from django import urls
from django.shortcuts import render, redirect
from django.http import HttpResponse
from httpx import get
from pydantic_core import Url
from app_a.models import MySpider
from .forms import UserInputForm  # Import the form if you have one
from .models import MySpider
from django.template import RequestContext
from .models import (scrape_data, user_fill_name, get_fill_type, create_file, get_user_input,
                     process_user_input, fetch_data_from_internet)

def index(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            entities, intent = process_user_input(user_input)
            # Create an instance of MySpider and call generate_urls method
            spider = MySpider(user_input)
            urls = spider.generate_urls()
            # Scrape data based on user input
            scrape_data(user_input)
            # Ask user for file name
            file_name = user_fill_name()
            # Ask user for file type and create the file
            MySpider(urls) # Pass urls to fill_type_handler
            # Redirect to the result page
            return redirect('result')
        else:
            return HttpResponse("Invalid form data.")
    else:
        form = UserInputForm()
    return render(request, 'index.html', {'form': form})

def result(request):
    return HttpResponse("This is the result view.")
def create_file_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            entities,intent = process_user_input(user_input)
            # Scrape data based on user input
            scrape_data(user_input)
            # Ask user for file name
            file_name = user_fill_name()
            # Ask user for file type
            fill_type = get_fill_type()  # You need to implement get_fill_type function
            if fill_type:
                # Create the file
                creation_message = create_file(file_name, fill_type, urls)  # urls should be provided
                return render(request, 'result.html', {'message': creation_message})
            else:
                return HttpResponse("Invalid file type.")
        else:
            return HttpResponse("Invalid form data.")
    else:
        form = UserInputForm()
    return render(request, 'index.html', {'form': form})
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

