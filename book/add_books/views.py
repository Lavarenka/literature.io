from pyexpat.errors import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import AddBookForm
from django.views.generic import CreateView, View
from django.contrib.messages.views import SuccessMessageMixin



def add_book(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        content = request.GET.get('content')
        mail = request.GET.get('mail')
        if title and content:
            my_obj = AddBook(title=title, content=content, mail=mail)
            my_obj.save()
            messages.add_message(request, messages.INFO, 'Форма отправлена! ')
            return redirect('home')
    return render(request, 'add_books/add_book.html')




