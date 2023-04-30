from django import forms

from .models import Artwork


class ArtworkForm(forms.ModelForm):
    file = forms.ImageField()

    class Meta:
        model = Artwork
        fields = (
            'title',
            'description',
            'tags',
        )
