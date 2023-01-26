from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Thread, Comment
from .forms import ThreadForm, CommentForm


def Home(request):
    return render(request, "index.html")


class ThreadList(generic.ListView):
    """ View for rendering all build threads """
    model = Thread
    queryset = Thread.objects.order_by('-post_date')
    template_name = 'blog_lists.html'
    paginate_by = 6


class ThreadDetail(View):
    """ View for redering thread details """
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


class UserThreads(generic.ListView):
    def get(self, request):
        if request.user.is_authenticated:
            threads = Thread.objects.filter(author=request.user)
            paginator = Paginator(threads, 4)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'my_threads.html', {'page_obj': page_obj})
        else:
            return render(request, 'my_threads.html')


class AddThread(View):
    """ View for user to create a build thread """
    def get(self, request):

        return render(request, "create_thread.html", {"thread_form":
                                                      ThreadForm()})

    def post(self, request):

        thread_form = ThreadForm(request.POST, request.FILES)

        if thread_form.is_valid():
            thread = thread_form.save(commit=False)
            thread.author = request.user
            thread.slug = slugify('-'.join([str(thread.author),
                                           str(thread.make),
                                           str(thread.model)]),
                                  allow_unicode=False)
            thread.save()
            messages.success(request,
                             'The build has been created successfully')
            return redirect('my_threads')
        else:
            thread_form = ThreadForm()

            return render(
                request, "create_thread.html",
                {
                    "thread_form": thread_form
                },
            )


class EditThread(UpdateView):
    """ View to Edit Thread post """
    model = Thread
    template_name = 'edit_thread.html'
    form_class = ThreadForm
    success_url = reverse_lazy('my_threads')


class EditComment(UpdateView):
    """ View to Edit Comments """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'Comment Successfully Updated'


@login_required
def delete_thread(request, pk):
    """ View to Delete Thread post """
    print("hello")
    thread = get_object_or_404(Thread, id=pk)
    if thread.author.id == request.user.id:
        thread.delete()
        messages.success(request, 'Build Thread Deleted Successfully')
    else:
        messages.error(request, "Unauthorised action")
    return redirect(reverse('my_threads'))


class ThreadLike(View):
    """ View for thread like functionality """
    def post(self, request, slug):
        thread = get_object_or_404(Thread, slug=slug)

        if thread.likes.filter(id=request.user.id).exists():
            thread.likes.remove(request.user)
        else:
            thread.likes.add(request.user)

        return HttpResponseRedirect(reverse('thread_detail', args=[slug]))


class Featured(View):

    def get(self, request):
        featured_threads = Thread.objects.filter(featured=True)[:2]
        context = {
            "featured_threads": featured_threads,
        }
        return render(request, 'featured.html', context)


def About(request):
    """return response"""
    return render(request, "about.html")


def Partners(request):
    return render(request, "partners.html")


def error_404(request, exception):
    """ View for 404 error """
    return render(request, "404_page.html", status=404)


def error_500(request):
    """ View for 500 error """
    return render(request, '500_page.html', status=500)
