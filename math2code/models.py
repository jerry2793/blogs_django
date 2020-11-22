from django.db import models

from PIL import Image
User = ''

# Create your models here.
class Math2codeCommentReplies(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    # comment = models.ForeignKey(Math2codeComments,models.CASCADE)

    # reply_to_comment = models.BooleanField
    # reply_to = models.AutoField()
    reply = models.CharField(max_length=500,blank=False)

    date_added = models.DateTimeField(auto_now_add=True)


class Math2codeComments(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    # article = models.ForeignKey(Math2codeContent,models.CASCADE)

    # reply_to_comment = models.BooleanField(default=False)
    reply_to = models.CharField(max_length=100000000)
    replies = models.ForeignKey(Math2codeCommentReplies,models.CASCADE)

    comment = models.CharField(max_length=1000, blank=False)

    date_added = models.DateTimeField(auto_now_add=True)


class Math2codeContent(models.Model):
    title = models.CharField(max_length=100,blank=False)
    header_image = models.ImageField(upload_to="math2code/images/")
    description = models.CharField(max_length=250,blank=True)
    author = models.ForeignKey(User,models.CASCADE)

    problem = models.TextField(blank=False)
    explaination_problem = models.TextField(blank=False)

    code = models.FileField(blank=False,upload_to="math2code/code")
    code_type = models.CharField(max_length=25,choices=(
        ('1','Python'),
        ('2','JavaScript'),
    ), default='1')
    explaination_code = models.TextField(blank=False)

    comments = models.ForeignKey(Math2codeComments,models.CASCADE)
    url = models.URLField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)


class Math2codeArticle(models.Model):
    # here is the actual article object to reference
    article = models.ForeignKey(Math2codeContent,models.CASCADE)
    comments = models.ForeignKey(Math2codeComments,models.CASCADE)

