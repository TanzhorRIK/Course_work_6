from django.utils.text import slugify
from blog.models import BlogPost
from django import forms

EXCLUTION_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                   'бесплатно', 'обман', 'полиция', 'радар']

class BlogPostForm(forms.ModelForm):


    class Meta:
        model = BlogPost
        exclude = ['created_at', 'views_count', 'slug', 'user']

    def clean_title(self):
        cleaned_data = self.cleaned_data['name']
        cnt = 0
        for item in EXCLUTION_WORDS:
            if item == cleaned_data.lower():
                cnt += 1

        if cnt > 0:
            raise forms.ValidationError("слово запрещено")
        return cleaned_data

    def clean_content(self):

        cleaned_data = self.cleaned_data.get('content')
        if cleaned_data in EXCLUTION_WORDS:
            raise forms.ValidationError('слово запрещено')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
