from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description']

    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)

    def clean_title(self):
        title = self.cleaned_data['title']
        # Check if a content object with the same title already exists
        if Content.objects.filter(title=title).exists():
            raise forms.ValidationError('A content with this title already exists.')
        return title 