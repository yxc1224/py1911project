from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "url", "body"]
        labels = {
            "name": "名字:",
            "email": "邮箱:",
            "url": "网址:",
            "body": "评论:"
        }
        widgets = {
            "body":forms.Textarea()
        }
