from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.decorators import login_required

from .models import Math2codeContent,Math2codeComments
from .forms import Math2codeCommentsForm,Math2codeCommentRepliesForm

Articles = Math2codeContent
Comments = Math2codeComments


# Create your views here.
class IndexView(View):
    def get(self,*args,**kwargs):
        ctx = {
            'posts':Articles.objects.all()
        }
        return render(self.request,'math2code/index.html',ctx)

    def post(self,*args,**kwargs):
        pass


class ArticlesView(View):
    def __init__(self,*args,**kwargs):
        self.templates = {
            'article':'math2code/article.html'
        }
        self.pk = self.kwargs['pk']

        self.request.POST['user'] = self.request.user

        self.CommentForm = Math2codeCommentsForm(self.request.POST)
        self.ReplyForm = Math2codeCommentRepliesForm(self.request.POST)

        self.ctx = {
            'article':Articles.objects.filter(id=self.pk),
            'comments':Comments.objects.filter(reply_to=str(self.pk)),
            'commentForm': self.CommentForm,
            'replyForm': self.ReplyForm,
        }
        self.submitted_form = self.check_submitted_form(self.request.POST)


    def get(self,*args,**kwargs):
        
        return render(self.request,self.templates['article'],self.ctx)


    @login_required
    def post(self,*args,**kwargs):
        if self.submitted_form.is_valid():
            self.submitted_form.save()
        else:
            return render(self.request,self.templates['article'],self.ctx)

    def check_submitted_form(self,POST):
        if POST['submit'] == 'comment-btn':
            self.CommentForm['article'] = self.ctx['article']
            return self.CommentForm
        else:
            self.ReplyForm['comment'] = POST['submit']
            return self.ReplyForm