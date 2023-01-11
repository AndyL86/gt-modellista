from django.shortcuts import render
from django.views import generic, View
from .models import Thread


def Home(request):
    # return response
    return render(request, "index.html")


class ThreadList(generic.ListView):
    model = Thread
    queryset = Thread.objects.order_by('-post_date')
    template_name = 'blog-list-gtm.html'
    paginate_by = 6


def BlogList(request):
    # return response
    return render(request, "blog-select.html")


def About(request):
    # return response
    return render(request, "about.html")
