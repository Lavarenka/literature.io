from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import AddBook
from django.contrib import messages


def add_book(request):
    """
    we accept the get request and save it to the database.
    mail is transmitted automatically
    """
    if request.method == 'GET':
        title = request.GET.get('title')
        content = request.GET.get('content')
        mail = request.GET.get('mail')
        if title and content:
            my_obj = AddBook(title=title, content=content, mail=mail)
            my_obj.save()
            messages.add_message(request, messages.INFO, 'Форма отправлена! ')
            return redirect('home')
    return render(request, 'add_books/add_book.html', {'title': 'Предложить книгу'})
