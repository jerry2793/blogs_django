from django.db import models

from PIL import Image

from profile.models import Profile as User

from datetime import datetime


# Create your models here.
class Math2codeContent(models.Model):
    title = models.CharField(max_length=100,blank=False)
    header_image = models.ImageField(upload_to="math2code/images/")
    description = models.CharField(max_length=250,blank=True)
    author = models.ForeignKey(User,models.CASCADE,default=None,blank=True)

    problem = models.TextField(blank=False)
    explaination_problem = models.TextField(blank=False)

    code = models.FileField(blank=False,upload_to="math2code/code")
    code_type = models.CharField(max_length=25,choices=(
        ('1','Python'),
        ('2','JavaScript'),
    ), default='1')
    explaination_code = models.TextField(blank=False)

    # comments = models.ForeignKey(Math2codeComments,models.CASCADE)
    url = models.URLField(default=None,max_length=100,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    when_publish = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class Math2codeComments(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    article = models.ForeignKey(Math2codeContent,models.CASCADE,default=0)
    comment = models.CharField(max_length=1000, blank=False)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Math2codeCommentReplies(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    comment = models.ForeignKey(Math2codeComments,models.CASCADE)

    # reply_to_comment = models.BooleanField
    # reply_to = models.CharField(max_length=100000)
    reply = models.CharField(max_length=500,blank=False)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply





# class Math2codeArticle(models.Model):
#     # here is the actual article object to reference
#     article = models.ForeignKey(Math2codeContent,models.CASCADE)
#     comments = models.ForeignKey(Math2codeComments,models.CASCADE)

