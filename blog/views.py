from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Thread
from .forms import ThreadForm, CommentForm


def Home(request):
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
              "commented": False,
              "liked": liked,
              "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):
        queryset = Thread.objects.all()
        thread = get_object_or_404(queryset, slug=slug)
        comments = thread.thread_comments.order_by('comment_date')
        liked = False
        if thread.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.thread = thread
            comment.save()
            messages.success(request, 'Comment added successfully')
        else:
            comment_form = CommentForm()
            messages.error(request, 'Error posting comment')

        return render(
            request,
            "thread_detail.html",
            {
              "thread": thread,
              "comments": comments,
              "commented": True,
              "liked": liked,
              "comment_form": CommentForm()
            },
        )


class AddThread(CreateView):

    model = Thread
    form_class = ThreadForm
    template_name = 'create_thread.html'
    success_url = reverse_lazy('thread-list-gtm')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ThreadLike(View):
    """Post like functionality"""
    def post(self, request, slug):
        thread = get_object_or_404(Thread, slug=slug)

        if thread.likes.filter(id=request.user.id).exists():
            thread.likes.remove(request.user)
        else:
            thread.likes.add(request.user)

        return HttpResponseRedirect(reverse('thread_detail', args=[slug]))


def BlogList(request):
    """return response"""
    return render(request, "blog-select.html")


def About(request):
    """return response"""
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def Partners(request):
    return render(request, "partners.html")
