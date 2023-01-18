from .models import Comment
from django import forms


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
