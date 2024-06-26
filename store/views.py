from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    context = {
        'page': "Mystery Books",
    }
    return render(request, 'store/template.html', context)

def store(request):
    books = Book.objects.all()
    context = {
        'page': "Welcome to Mystery Books",
        'book_count': Book.objects.all().count(),
        'books': books,
    }
    return render(request, 'store/store.html', context)

def new_book(request):
    if request.method == 'POST':
        page = "The book has been created"
        show_form = False
        try:
            Book.objects.create(
                author=request.POST.get('author'), # name field in form
                title=request.POST.get('title'), # title field in form
                description=request.POST.get('description'), # description field in form
                publish_date=request.POST.get('publish_date'),
                price=request.POST.get('price'), # price field in form
                stock=request.POST.get('stock'),
            )
        except Exception as e:
            print(e)
            page = "Error creating book. Try again later."
            error_message = str(e)
    else:
        page = 'New Book'
        show_form = True
    context = {
        'page': page,
        'show_form': show_form,
        'error_message': error_message,
    }
    return render(request, 'store/new_book.html', context)