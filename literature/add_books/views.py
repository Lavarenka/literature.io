from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import *
from .forms import NewsForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin


# def Add_Book(request):
#     """
#     cleaned_data // рендерит словарь с входными данным, без него будет просто html
#     """
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect('add_book')
#     else:
#         form = NewsForm()
#     return render(request, 'add_books/add_book.html', {'form': form})



class AddBook( SuccessMessageMixin , CreateView):
    """
    LoginRequiredMixin // не пускает и делает редирект для неавторизованного пользователя
    """
    form_class = NewsForm # форма
    template_name = 'add_books/add_book.html'
    success_url = '/' # редирект на главную после отправки формы

    success_message = "Форма отправлена"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Предложить книгу'

        return context
