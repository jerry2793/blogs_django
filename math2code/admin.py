from django.contrib import admin

from .models import (
    Math2codeContent,
    Math2codeComments,
    Math2codeCommentReplies
)
# Register your models here.
admin.site.register(Math2codeContent)
admin.site.register(Math2codeComments)
admin.site.register(Math2codeCommentReplies)