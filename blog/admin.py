from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Thread, Comment


@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):
    """Admins Thread model features"""
    summernote_fields = ('story', 'modifications')
    list_display = ('year', 'make', 'model', 'post_date',
                    'featured')
    prepopulated_fields = {'slug': ('year', 'make', 'model')}
    list_filter = ('post_date', 'author', 'featured')
    search_fields = ['make', 'model', 'year']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Admins Comment model features """
    list_display = ('name', 'body', 'comment_date', 'thread')
    list_filter = ('comment_date',)
    search_fields = ['name', 'body']
