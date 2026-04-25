from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from book.forms import BookForm
from book.models import Book

# Create a new book
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book-list')  # More natural redirect
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})

# List all books
def book_list(request):
    genre = request.GET.get('genre')
    if genre:
             books = Book.objects.filter(genre=genre).order_by('-created_at')     
    else:
        books = Book.objects.all().order_by('-created_at')  # Optional: .order_by('-created_at')
    return render(request, 'book/book_list.html', {'books': books})

# View book detail
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

# Update book
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book-update', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('book-list')