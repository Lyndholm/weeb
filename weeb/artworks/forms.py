from django import forms

from .models import Artwork


class ArtworkCreateForm(forms.ModelForm):
    file = forms.ImageField()

    class Meta:
        model = Artwork
        fields = (
            'title',
            'description',
            'tags',
        )


class ArtworkEditForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = (
            'title',
            'description',
            'tags',
        )
