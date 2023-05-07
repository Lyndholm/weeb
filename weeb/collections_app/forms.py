from django import forms

from .models import Collection


class CollectionCreateForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = (
            'name',
            'description',
            'cover_image',
            'is_public',
        )

    def save(self, request, commit=True):
        collection = super().save(commit=False)
        collection.author = request.user

        if commit:
            collection.save()
            self.save_m2m()

        return collection
