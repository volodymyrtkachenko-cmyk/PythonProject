from django import forms
from .models import Post, Comment, Subscribe


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date', 'user')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('published_date','post', 'user')


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('user_name','email',)


