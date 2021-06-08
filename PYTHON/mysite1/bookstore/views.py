from unicodedata import decimal

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book


def index_view(request):
    return HttpResponse('bookstore')
    # return render(request,'boo/index.html')

def all_book(request):
    # book = Book()
    # book.title='D'
    # book.info='DD'
    # book.price=35
    # book.save()
    all_book = Book.objects.all()
    return render(request, 'bookstore/all_book.html',locals())

def query_book(request,title):
    query_book = Book.objects.filter(title=title)
    return render(request, 'bookstore/list_book.html', locals())

def get_book(request,title):
    book = Book.objects.get(title=title)
    return render(request, 'bookstore/get_book.html', locals())

def query_price_book(request,price):
    query_book = Book.objects.filter(price__gte=price)
    return render(request, 'bookstore/list_book.html', locals())

def update_book(request,book_id):
    print(book_id)
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        print('update error')
        return HttpResponse('update error')

    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html',locals())
    elif request.method == 'POST':
        price = request.POST['price']
        info = request.POST['info']
        book.price = price
        book.info = info
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')

def delete_book(request,book_id):
    print(book_id)
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return HttpResponseRedirect('/bookstore/all_book')
    except Exception as e:
        print('delete error')
        return HttpResponse('delete error')

