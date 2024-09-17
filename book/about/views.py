from django.shortcuts import render


def about(request):
    """ about us page render """
    return render(request, 'about/about.html', {'title': 'О нас'})
