from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ArtworkForm
from .models import Artwork, ImageFile, Tag


def home_page(request):
    artworks = Artwork.objects.all().order_by('-published_at')
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
    form = ArtworkForm()
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)

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
def delete_artwork(request, pk):
    artwork = Artwork.objects.get(id=pk)

    if request.user != artwork.author:
        raise Http404  # TODO: Return 403 Forbidden

    if request.method == 'POST':
        artwork.file.delete()  # TODO: Also delete artwork file from storage (signals)
        return redirect('home-page')

    context = {'obj': f'арт "{artwork.title}"'}
    return render(request, 'delete.html', context)
