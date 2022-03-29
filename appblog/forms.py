from django import forms

class PostForm (forms.Form):
    content = forms.CharField(max_length=4000)
    author = forms.CharField(max_length=100)

class UserSearchForm (forms.Form):
    user = forms.CharField(max_length=100)
