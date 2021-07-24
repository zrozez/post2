from django import forms
from django.forms import fields
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', ]

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class SearchForm(forms.Form):

    search_param = forms.CharField(widget = forms.TextInput(attrs={'class': "form-control me-2", 'type':"search", "placeholder":"Search", "aria-label":"Search"}))

def add_search_form(request):
    return {'search_form': SearchForm()}