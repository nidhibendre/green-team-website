from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    other_author = forms.CharField(max_length=100, required=False, label="Other Author")
    
    class Meta:
        model = BlogPost
        fields = ['cover_photo', 'cover_source', 'author', 'other_author', 'title', 'subtitle', 'body_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subtitle'].widget.attrs['placeholder'] = 'Optional'
        self.fields['author'].required = False
        self.fields['author'].widget.attrs['onchange'] = "check_other_author(this.value);"


