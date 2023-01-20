from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .models import Thread
from .forms import ThreadForm, CommentForm


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
        else:
            comment_form = CommentForm()

        return render(
            request,
            'thread_detail.html',
            {
              "thread": thread,
              "comments": comments,
              "commented": True,
              "liked": liked,
              "comment_form": CommentForm()
            },
        )


class AddThread(CreateView):

    def get(self, request):

        return render(request, "create_thread.html", {"thread_form":
                      ThreadForm()})

    def post(self, request):

        thread_form = ThreadForm(request.POST, request.FILES)

        if thread_form.is_valid():
            thread = thread_form.save(commit=False)
            thread.author = request.user
            thread.slug = slugify('-'.join([str(thread.author),
                                  str(thread.year),
                                           thread.make, thread.model]),
                                  allow_unicode=False)
            thread.save()
            messages.success(request,
                             'Build Thread Successfully Uploaded')
            return redirect('thread-detail.html')
        else:
            thread_form = ThreadForm()

            return render(
                request, "create_thread.html",
                {
                    "thread_form": thread_form
                },
            )


class ThreadLike(View):
    # Post like functionality
    def post(self, request, slug):
        thread = get_object_or_404(Thread, slug=slug)

        if thread.likes.filter(id=request.user.id).exists():
            thread.likes.remove(request.user)
        else:
            thread.likes.add(request.user)

        return HttpResponseRedirect(reverse('thread_detail', args=[slug]))


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
