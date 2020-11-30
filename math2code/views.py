from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from profile.models import Profile

from .models import Math2codeContent,Math2codeComments,Math2codeCommentReplies
from .forms import (
    Math2codeContentForm,
    Math2codeCommentsForm,
    Math2codeCommentRepliesForm
    )
ArticleCreateForm = Math2codeContentForm
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

# @method_decorator(login_required,name='post')
class ArticlesView(View):
    # def my_init(self,*args,**kwargs):
    #     self.templates = {
    #         'article':'math2code/article.html'
    #     }
    #     self.pk = self.kwargs['pk']


    #     self.CommentForm = Math2codeCommentsForm(self.request.POST)

    #     self.ctx = {
    #         'article':Articles.objects.filter(id=self.pk),
    #         'comments':Comments.objects.filter(reply_to=str(self.pk)),
    #         'commentForm': self.CommentForm,
    #         'replyForm': self.ReplyForm,
    #     }
    #     self.submitted_form = self.check_submitted_form(self.request.POST)


    def get(self,*args,**kwargs):
        pk = self.kwargs['pk']
        CommentForm = Math2codeCommentsForm()
        ReplyForm = Math2codeCommentRepliesForm()
        ctx = {
            'article':Articles.objects.get(id=pk),
            'comments':Comments.objects.filter(article=pk),
            'commentForm': CommentForm,
            'replyForm': ReplyForm,
            'replies':Math2codeCommentReplies.objects.filter(article=pk).all(),
        }
        return render(self.request,'math2code/article.html',ctx)


    # def post(self,*args,**kwargs):
    #     pk = self.kwargs['pk']
    #     CommentForm = Math2codeCommentsForm
    #     ReplyForm = Math2codeCommentRepliesForm
    #     # self.request.POST['user'] = self.request.user
    #     postData = self.request.POST
    #     submitted_form = self.check_submitted_form(postData)
    #     ctx = {
    #         'article':Articles.objects.get(id=pk),
    #         'comments':Comments.objects.filter(article=pk),
    #         'commentForm': CommentForm,
    #         'replyForm': ReplyForm,
    #     }
    #     if submitted_form.is_valid():
    #         print(submitted_form.cleaned_data)
    #         # submitted_form.save(commit=False)
    #         # submitted_form.user = self.request.user.id
    #         submitted_form.save()
    #         return render(self.request,'math2code/article.html',ctx)
    #     else:
    #         return render(self.request,'math2code/article.html',ctx)

@login_required
def handleCommentPost(request,*args,**kwargs):
    # article_pk = kwargs['pk']
    if request.POST:
        user = Profile.objects.get(user=request.user)
        article = Articles.objects.get(pk=request.POST['article'])
        Comments.objects.create(user=user,article=article,comment=request.POST['comment'])
        return redirect('math2code-articles',pk=request.POST['article'])

@login_required
def handleReplyPost(request, *args, **kwargs):
    if request.POST:
        user = Profile.objects.get(user=request.user)
        article = Articles.objects.get(pk=request.POST['article'])
        Math2codeCommentReplies.objects.create(
            article=article, 
            user=user,
            reply=request.POST['reply']
        )
        return redirect('math2code-articles',pk=request.POST['article'])
    else:
        print('requested a get')
        


    def check_submitted_form(self,POST):
        if POST['submit'] == 'Comment':
            return Math2codeCommentsForm(POST)
        else:
            return Math2codeCommentRepliesForm(POST)



class ArticleCreateView(View):
    def __init__(self):
        self.template = {
            'write-article':'math2code/write-article.html',
            'success':'math2code/new-article_success.html'
        }

        self.request.POST['author'] = self.request.user

        self.ctx = {
            'create-form':ArticleCreateForm(self.request.POST)
        }
        self.new_article = self.ctx['create-form']


    def get(self,*args,**kwargs):
        return render(self.request,self.template['write-article'], self.ctx)

    
    def post(self,**kwargs):
        if self.new_article.is_valid:
            self.new_article.save()
            return render(self.request,self.template['success'], self.ctx)
        else:
            return render(self.request,self.template['write-article'], self.ctx)