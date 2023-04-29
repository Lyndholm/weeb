from django.db.models import Count
from django.shortcuts import render

from .models import Artwork, Tag


def home_page(request):
    artworks = Artwork.objects.all()
    all_tags_count = Tag.objects.all().count()
    popular_tags = Tag.objects.annotate(num_artworks=Count('artwork_tags')).order_by(
        '-num_artworks'
    )[:10]
    context = {
        'artworks': artworks,
        'all_tags_count': all_tags_count,
        'popular_tags': popular_tags,
    }

    return render(request, 'home.html', context)
