from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Book, Address, Student, Publisher, Author

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def lab5_links(request):
    return render(request, 'bookmodule/links.html')
def lab5_formatting(request):
    return render(request, 'bookmodule/formatting.html')
def lab5_listing(request):
    return render(request, 'bookmodule/listing.html')
def lab5_tables(request):
    return render(request, 'bookmodule/tables.html')
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765, 'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    return render(request, 'bookmodule/search.html')
def insert_books(request):
    Book.objects.create(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.00, edition=3)
    Book.objects.create(title='Reversing: Secrets of Reverse Engineering', author='E. Eilam', price=97.00, edition=2)
    Book.objects.create(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.00, edition=4)
    return render(request, 'bookmodule/index.html')
def simple_query(request):
    mybooks = Book.objects.filter(author__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(author__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
def insert_more_books(request):
    Book.objects.create(title='Clean Code', author='Robert Martin', price=75.00, edition=1)
    Book.objects.create(title='The Pragmatic Programmer', author='Andrew Hunt', price=60.00, edition=2)
    Book.objects.create(title='Introduction to Algorithms', author='Cormen et al', price=80.00, edition=4)
    Book.objects.create(title='Quantum Computing', author='Qudrat Abdullayev', price=55.00, edition=5)
    return render(request, 'bookmodule/index.html')
def lab8_task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})
def lab8_task2(request):
    mybooks = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})
def lab8_task3(request):
    mybooks = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})
def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})
def lab8_task5(request):
    data = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'data': data})
def insert_students(request):
    city1 = Address.objects.create(city='Riyadh')
    city2 = Address.objects.create(city='Jeddah')
    city3 = Address.objects.create(city='Qassim')

    Student.objects.create(name='Ali', age=20, address=city1)
    Student.objects.create(name='Sara', age=22, address=city1)
    Student.objects.create(name='Ahmed', age=21, address=city2)
    Student.objects.create(name='Mona', age=23, address=city3)
    Student.objects.create(name='Khalid', age=19, address=city1)

    return render(request, 'bookmodule/index.html')

def lab8_task7(request):
    from django.db.models import Count
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'cities': cities})

def insert_lab9_data(request):
    # Create Publishers
    pub1 = Publisher.objects.create(name='Pearson', location='London')
    pub2 = Publisher.objects.create(name='OReilly', location='New York')
    pub3 = Publisher.objects.create(name='Springer', location='Berlin')

    # Create Authors
    auth1 = Author.objects.create(name='Robert Martin', DOB='1952-12-05')
    auth2 = Author.objects.create(name='Andrew Hunt', DOB='1964-03-15')
    auth3 = Author.objects.create(name='Donald Knuth', DOB='1938-01-10')

    # Create Books
    b1 = Book.objects.create(title='Clean Code', price=75.0, quantity=3, pubdate='2024-01-01 00:00:00', rating=5, publisher=pub1)
    b1.authors.add(auth1)

    b2 = Book.objects.create(title='The Pragmatic Programmer', price=60.0, quantity=6, pubdate='2022-05-10 00:00:00', rating=4, publisher=pub1)
    b2.authors.add(auth2)

    b3 = Book.objects.create(title='Introduction to Algorithms', price=80.0, quantity=2, pubdate='2020-08-20 00:00:00', rating=3, publisher=pub2)
    b3.authors.add(auth3)

    b4 = Book.objects.create(title='Quantum Computing', price=55.0, quantity=4, pubdate='2023-03-15 00:00:00', rating=5, publisher=pub2)
    b4.authors.add(auth1)

    b5 = Book.objects.create(title='Continuous Delivery', price=120.0, quantity=1, pubdate='2021-11-01 00:00:00', rating=2, publisher=pub3)
    b5.authors.add(auth2)

    b6 = Book.objects.create(title='Reversing', price=97.0, quantity=7, pubdate='2019-06-30 00:00:00', rating=4, publisher=pub3)
    b6.authors.add(auth3)

    return render(request, 'bookmodule/index.html')

def lab9_task1(request):
    books = Book.objects.all()
    total_quantity = sum(book.quantity for book in books)
    for book in books:
        book.percentage = round((book.quantity / total_quantity) * 100, 2)
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

def delete_old_books(request):
    Book.objects.filter(publisher__isnull=True).delete()
    return render(request, 'bookmodule/index.html')

def lab9_task2(request):
    from django.db.models import Sum
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

def lab9_task3(request):
    from django.db.models import Min
    publishers = Publisher.objects.annotate(oldest_pubdate=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})

def lab9_task4(request):
    from django.db.models import Avg, Min, Max
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

def lab9_task5(request):
    from django.db.models import Count, Sum, Q
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4)),
        high_rated_quantity=Sum('book__quantity', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})

def lab9_task6(request):
    from django.db.models import Count, Q
    publishers = Publisher.objects.annotate(
        book_count=Count('book', filter=Q(
            book__price__gt=50,
            book__quantity__lt=5,
            book__quantity__gte=1
        ))
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})
