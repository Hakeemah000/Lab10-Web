from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

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

def search(request):
    return render(request, 'bookmodule/books/search.html')

def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        # استرجاع البيانات من النموذج
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # استرجاع قائمة الكتب
        books = __getBooksList()
        newBooks = []

        # تصفية الكتب بناءً على الكلمة المفتاحية
        for item in books:
            contained = False
            # تحقق من وجود الكلمة المفتاحية في العنوان إذا كان الخيار محددًا
            if isTitle and string in item['title'].lower():
                contained = True
            # تحقق من وجود الكلمة المفتاحية في المؤلف إذا كان الخيار محددًا
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            # أضف الكتاب إلى النتائج إذا كان يحتوي على الكلمة المفتاحية
            if contained:
                newBooks.append(item)

        # عرض النتائج في القالب `bookList.html`
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    # عرض النموذج إذا لم يكن الطلب `POST`
    return render(request, 'bookmodule/search.html')


def add_books(request):
    # الكتاب الأول
    mybooks = Book(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.0, edition=3)
    mybooks.save()  # حفظ الكتاب الأول

    # الكتاب الثاني
    mybooks = Book(title='Reversing: Secrets of Reverse Engineering', author='E. Eilam', price=97.0, edition=2)
    mybooks.save()  # حفظ الكتاب الثاني

    # الكتاب الثالث
    mybooks = Book(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.0, edition=4)
    mybooks.save()  # حفظ الكتاب الثالث

    return HttpResponse("Books added successfully!")

def simple_query(request):
    mybooks = Book.objects.all()  # جلب جميع الكتب
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lookup_query(request):
    # استخدام دوال التصفية المتقدمة (complex query)
    mybooks = Book.objects.filter(author__isnull=False) \
                          .filter(title__icontains='and') \
                          .filter(edition__gte=2) \
                          .exclude(price__lte=100)[:10]
    
    # إذا كانت هناك كتب تتوافق مع الشروط
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        # إذا لم تكن هناك نتائج، قم بإعادة توجيه المستخدم إلى الصفحة الرئيسية
        return render(request, 'bookmodule/index.html')

