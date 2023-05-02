from dal import autocomplete
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
        widgets = {
            'tags': autocomplete.ModelSelect2Multiple(url='tags-autocomplete'),
        }


class ArtworkEditForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = (
            'title',
            'description',
            'tags',
        )
        widgets = {
            'tags': autocomplete.ModelSelect2Multiple(url='tags-autocomplete'),
        }
