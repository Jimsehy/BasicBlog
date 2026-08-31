from django import forms

from blog.models import Post

class PostCreateForm(forms.ModelForm):
        fields = ['title', 'header_image', 'title_tag', 'author', 'body', 'snippet', 'category']

        class Meta:
            model = Post
            fields = ['title', 'header_image', 'title_tag', 'author', 'body', 'snippet', 'category']

            widgets = {
                'title':
                    forms.TextInput(attrs={'class': 'form-control'}),
                'header_image':
                    forms.FileInput(attrs={'class': 'form-control'}),
                'title-tag':
                    forms.TextInput(attrs={'class': 'form-control'}),
                'author':
                    forms.Select(attrs={'class': 'form-control'}),
                'body':
                    forms.Textarea(attrs={'class': 'form-control'}),
                'snippet':
                    forms.Textarea(attrs={'class': 'form-control'}),
                'category':
                    forms.Select(attrs={'class': 'form-control'}),

            }