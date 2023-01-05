from django.db import models
from django.contrib.auth.models import  User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Thread(models.Model):
    """ Build Thread model """
    year = models.PositiveSmallIntegerField()
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name="build_threads")
    updated_date = models.DateTimeField(auto_now=True)
    engine = models.PositiveSmallIntegerField()
    bhp = models.PositiveSmallIntegerField()
    story = models.TextField()
    modifications = models.TextField()
    thread_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="thread_likes",
                                   blank=True)
    
    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """ Returns number of likes """
        return self.likes.count()


class Comment(models.Model):
    """ Thread user comments model """
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='thread_comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"