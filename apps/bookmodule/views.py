from django.shortcuts import render

from django.http import HttpResponse
def index(request):
 name = request.GET.get("name") or "world!" #add this line
 return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name
 return render(request, "bookmodule/index.html" , {"name": name}) 

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))
def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)


def links(request):
    return render(request, 'bookmodule/books/links.html')

def formatting(request):
    return render(request, 'bookmodule/books/formatting.html') 

def listing(request):
    return render(request, 'bookmodule/books/listing.html')

def tables(request):
    return render(request, 'bookmodule/books/tables.html')

def index(request):
 return render(request, "bookmodule/books/index.html")
def list_books(request):
 return render(request, 'bookmodule/books/list_books.html')
def one_book(request, bookId):
    return render(request, 'bookmodule/books/one_book.html', {'bookId': bookId})
def aboutus(request):
 return render(request, 'bookmodule/books/aboutus.html')

def index(request):
    return render(request, 'bookmodule/index.html')


