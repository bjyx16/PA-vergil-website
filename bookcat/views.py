from django.shortcuts import render
from bookcat.models import Book
import io
import requests
# import pytesseract
# from PIL import Image
from bookcat.filters import BookFilter

def home(request):
    return render(request, "bookcat/home.html", {})

def bookcat_index(request): 
    books = Book.objects.all() #grabs all books from database; 
    
    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    
    context = {
        "books": books, #put all books as one object into dict for render function
        "myFilter": myFilter
    }
    return render(request, "bookcat/bookcat_index.html", context)

def bookcat_detail(request, pk): #pk = primary key; for individual book
    books = Book.objects.get(pk=pk)
    
    # if(books.image_str != None):
    #     response = requests.get(books.image_str)
    #     # print( type(response) ) # <class 'requests.models.Response'>
    #     img = Image.open(io.BytesIO(response.content))
    #     # print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
    #     text = pytesseract.image_to_string(img)
    # else:
    #     text = None

    context = {
        "book": books
    }
    return render(request, "bookcat/bookcat_detail.html", context)

