from django import forms

from .models import (
    Math2codeContent,
    Math2codeComments,
    Math2codeCommentReplies
)


class Math2codeContentForm(forms.ModelForm):
    class Meta: 
        paragraph_form = {
            'class':'paragraph-input'
        }
        model = Math2codeContent
        fields = (
            'title',
            'header_image',
            'description',

            'problem',
            'explaination_problem',

            'code',
            'code_type',
            'explaination_code',
        )


class Math2codeCommentsForm(forms.ModelForm):
    class Meta:
        model = Math2codeComments
        fields = ('comment',)


class Math2codeCommentRepliesForm(forms.ModelForm):
    class Meta:
        model = Math2codeCommentReplies
        fields = ('reply',)