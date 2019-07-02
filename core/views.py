
from django.shortcuts import render
from core.models import Book, Category
from django.views import generic

def index(request):
    book_list = Book.objects.all()

    context = {'book-list': book_list}

    return render(request, 'index.html', context=context)

    # return render(request,'index.html')

# def categories(request):
    # return render(request,'categories.html')

# def favorites(request):
#     return render(request,'favorites.html')

# def login(request):
#     return render(request,'login.html')



# class BookListView(generic.ListView):
#     model = Book
#     # def get_queryset(self):
#     #     return Book.objects.filter(title__icontains='')[:()]
# # ("def get_queryset" commented out because currently breaks site.)