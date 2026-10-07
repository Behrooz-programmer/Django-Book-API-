from django.shortcuts import render , get_object_or_404 , redirect
from .models import Book
from .forms import Bookform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required , permission_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import BookSerializer
from .permissions import IsEditorOrReadOnly

def books(request):
    query = request.GET.get('q','')

    if query:
        books = Book.objects.filter(title__icontains=query )| Book.objects.filter( author__icontains=query)
    else:
        books = Book.objects.all()

    paginator = Paginator(books,2)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)

    context = {
        "books": books,
        "page_title": "My Book Collection",
        'query' : query
    }

    return render(request, "books/books.html", context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    return render(request, 'books/book_detail.html' , {'book' : book})

@login_required
@permission_required('books.add_book', raise_exception=True)
def add_book(request):
    error = ''

    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        year = request.POST["year"]
        price = request.POST["price"]
        if not title or not author or not year or not price:
            error = "Please fill in all fields."
        else:
            try:
                year = int(year)
                price = int(price)

                Book.objects.create(title=title,author=author,year=year,price=price)
                messages.success(request, 'Create book successfully!')
                return redirect("books")

            except ValueError:
                error = "Year and price must be numbers."

    return render(request, "books/add_book.html" , {"error" : error})

@login_required
def form_test(request):
    if request.method == "POST":
        form = Bookform(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, 'Book saved successfully')

            form = Bookform()
    else:
        form = Bookform()

    return render(request, "books/form_test.html", {'form' : form})



@login_required
@permission_required("books.delete_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book,id = book_id)

    if request.method == 'POST':
        form = Bookform(request.POST, instance=book)

        if form.is_valid() :
            form.save()
            messages.success(request,'Book updated successfully!')
            return redirect('books')

    else:
        form = Bookform(instance = book)

    return render(request, 'books/edit_book.html',{'form' : form, 'book' : book})


@login_required
@permission_required("books.change_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id= book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request,'Book deleted successfully.')
        return redirect("books")

    return render(request, 'books/delete_book.html', {'book' : book})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("books")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("books")

        messages.error(request, "Invalid username or password.")

    return render(request, "books/login.html")

def logout_view(request):
    logout(request)
    return redirect('books')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('books')

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if User.objects.filter(username=username).exists():
            return render(request, 'books/register.html',{'error': 'Username already exists'})
        elif password != password2:
            return render(
                request, "books/register.html", {"error": "Passwords do not match."}
            )
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect ('books')


    return render(request, "books/register.html")

@api_view(["GET"])
def hello_api(request):
    return Response({"message": "Hello from Django REST Framework!"})

@api_view(["GET", "POST"])
@permission_classes([IsEditorOrReadOnly])
def book_api(request):

    if request.method == "POST":
        serializer = BookSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsEditorOrReadOnly])
def book_detail_api(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



    if request.method == "PATCH":
        serializer = BookSerializer(book, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        book.delete()
        return Response(status=204)







