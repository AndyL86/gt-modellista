from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Thread
from .forms import CommentForm


def Home(request):
    # return response
    return render(request, "index.html")


class ThreadList(generic.ListView):
    model = Thread
    queryset = Thread.objects.order_by('-post_date')
    template_name = 'blog-list-gtm.html'
    paginate_by = 6


class ThreadDetail(View):

    def get(self, request, slug):
        queryset = Thread.objects.all()
        thread = get_object_or_404(queryset, slug=slug)
        comments = thread.thread_comments.order_by('comment_date')
        liked = False
        if thread.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'thread_detail.html',
            {
              "thread": thread,
              "comments": comments,
              "liked": liked,
              "comment_form": CommentForm()
            },
        )


def BlogList(request):
    # return response
    return render(request, "blog-select.html")


def About(request):
    # return response
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def Partners(request):
    return render(request, "partners.html")
