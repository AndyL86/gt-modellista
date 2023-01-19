from .models import Thread, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


class ThreadForm(forms.ModelForm):
    """
    Create Build Thread Form
    """
    class Meta:
        model = Thread
        fields = ('year', 'make', 'model', 'thread_image', 'story',
                  'modifications', 'excerpt')

        widgets = {
            'story': SummernoteWidget(),
            'modifications': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.fields[
                'thread_image'
                ].label = "Upload an image:"


class CommentForm(forms.ModelForm):
    """
    Add Comment Form
    """
    class Meta:
        """
        Form Fields
        """
        model = Comment
        fields = ('body',)
