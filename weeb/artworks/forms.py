from dal import autocomplete
from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Artwork, ImageFile


class ArtworkCreateForm(forms.ModelForm):
    file = forms.ImageField()
    file.widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = Artwork
        fields = (
            'title',
            'description',
            'tags',
        )
        widgets = {
            'tags': autocomplete.ModelSelect2Multiple(
                url='autocomplete-tags-with-create-new'
            ),
        }

    def save(self, request, commit=True):
        artwork = super().save(commit=False)
        artwork.author = request.user

        file = self.cleaned_data.get('file')
        if isinstance(file, InMemoryUploadedFile):
            artwork.file = ImageFile.objects.create(file=file, uploaded_by=request.user)
        elif isinstance(file, ImageFile):
            artwork.file = file

        if commit:
            artwork.save()
            self.save_m2m()

        return artwork


class ArtworkEditForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = (
            'title',
            'description',
            'tags',
        )
        widgets = {
            'tags': autocomplete.ModelSelect2Multiple(
                url='autocomplete-tags-with-create-new'
            ),
        }
