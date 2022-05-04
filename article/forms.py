from django import forms


class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'article__comment-text',
        'cols': '30',
        'rows': '10'
    }))


