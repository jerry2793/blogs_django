from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

from .models import (
    Math2codeContent,
    Math2codeComments,
    Math2codeCommentReplies
)
from django.conf import settings

import os
from datetime import DateTime

BASE_URL = f'{settings.HOST_NAME}/math2code/articles/'

SERVER_EMAIL_ADDRESS = settings.EMAIL_HOST_USER

FAIL_SILENTLY = False

@receiver(post_save,sender=Math2codeContent)
def AppendURL(sender,**kwargs):
    sender.url = os.path.join(BASE_URL,sender.id)
    sender.save(update_fields=['id'])


# @receiver(post_save,sender=Math2codeCommentReplies)
def ReplyNotification(sender,**kwargs):
    send_mail(
        f'{sender.user.first_name} has replied to your comment on {sender.comment.article.title}',
        f"""
        Article Link: {sender.comment.article.url}
        Your Comment: {sender.comment.comment}
        Your Reply: {sender.rely}
        """,
        SERVER_EMAIL_ADDRESS,
        [f'{sender.comment.user.email}'],
        fail_silently=FAIL_SILENTLY
    )

# @receiver(post_save,sender=Math2codeContent)
def Math2codeContent_Email_Confirmation(sender,**kwargs):
    # if DateTime.now() >= sender.when_publish:
    send_mail(
        'Math TO Code Content Added!',
        f"""
        ID: {sender.id}
        Title: {sender.title}
        Problem: {sender.problem}
        Explaination to Problem: {sender.explaination_problem}
        """,
        'ruiyangandjerry@gmail.com',
        ['ruiyang_j2310@srcschools.org'],
        fail_silently=FAIL_SILENTLY
    )