from django.shortcuts import render
# You can keep HttpResponse if you want, but render is what uses the HTML files

def index(request):
    # This gets the name from the URL (?name=...) or defaults to "world!"
    name = request.GET.get("name") or "world!" 
    # This tells Django to use index.html and pass the 'name' variable
    return render(request, "bookmodule/index.html", {"name": name})

def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)