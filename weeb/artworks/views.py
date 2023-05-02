from dal import autocomplete
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ArtworkCreateForm, ArtworkEditForm
from .models import Artwork, ImageFile, Tag


def home_page(request):
    query = request.GET.get('query', '')

    artworks = (
        Artwork.objects.all()
        .order_by('-published_at')
        .filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(author__profile__nickname__iexact=query)
        )
    )
    all_tags_count = Tag.objects.all().count()
    popular_tags = Tag.objects.annotate(artworks_count=Count('artworks')).order_by(
        '-artworks_count'
    )[:10]
    context = {
        'artworks': artworks,
        'all_tags_count': all_tags_count,
        'popular_tags': popular_tags,
    }

    return render(request, 'home.html', context)


def artwork_page(request, pk):
    artwork = Artwork.objects.get(id=pk)
    context = {'artwork': artwork}
    return render(request, 'artwork.html', context)


@login_required(login_url='login')
def create_artwork(request):
    form = ArtworkCreateForm()
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = ArtworkCreateForm(request.POST, request.FILES)

        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.file = ImageFile.objects.create(
                file=request.FILES.get('file'),
                uploaded_by=request.user,
            )
            form.save()
            return redirect('home-page')

    context = {'form': form, 'tags': tags}
    return render(request, 'artwork_create.html', context)


@login_required(login_url='login')
def edit_artwork(request, pk):
    artwork = Artwork.objects.get(id=pk)
    form = ArtworkEditForm(instance=artwork)

    if request.user != artwork.author:
        raise Http404  # TODO: Raise 403 Forbidden

    if request.method == 'POST':
        # TODO: Ability for editing artwork file?
        form = ArtworkEditForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            artwork = form.save()
            return redirect('artwork', pk=artwork.pk)

    context = {'form': form}
    return render(request, 'artwork_edit.html', context)


@login_required(login_url='login')
def delete_artwork(request, pk):
    artwork = Artwork.objects.get(id=pk)

    if request.user != artwork.author:
        raise Http404  # TODO: Return 403 Forbidden

    if request.method == 'POST':
        artwork.file.delete()  # TODO: Also delete artwork file from storage (signals)
        return redirect('home-page')

    context = {'obj': f'арт "{artwork.title}"'}
    return render(request, 'delete.html', context)


def tags_page(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags})


class TagsAutocmplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tag.objects.all()

        if self.q:
            return qs.filter(name__istartswith=self.q)

        return qs
