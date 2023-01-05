from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Build, Comment


@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):
    """Admins Thread model features"""
    summernote_fields = ('story', 'modifications', 'feature_cap')
    list_display = ('author', 'year', 'make', 'model', 'post_date',
                    'featured')
    prepopulated_fields = {'slug': ('author', 'year', 'make', 'model')}
    list_filter = ('post_date', 'author', 'featured')
    search_fields = ['make', 'model', 'year']