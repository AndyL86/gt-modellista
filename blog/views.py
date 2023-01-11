from django.shortcuts import render
from django.views import generic, View
from .models import Thread


class ThreadList(generic.ListView):
    model = Thread
    queryset = Thread.objects.order_by('-post_date')
    template_name = 'index.html'
    paginate_by = 6

def BlogList(request):
    # return response
    return render(request, "blog-select.html")

def About(request):
    # return response
    return render(request, "about.html")
