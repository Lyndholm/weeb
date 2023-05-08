from artworks.models import Artwork
from artworks.views import paginate
from django import http
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CollectionCreateForm, CollectionEditForm
from .models import Collection, CollectionArtwork


def collections_home_page(request):
    collections = Collection.objects.all()
    collections = paginate(request, collections, 10)

    context = {'collections': collections}
    return render(request, 'collections.html', context)


def collection_page(request, pk):
    collection = Collection.objects.get(id=pk)
    context = {'collection': collection}
    return render(request, 'collection.html', context)


@login_required(login_url='login')
def user_collections(request):
    context = {'collections': request.user.collections.all()}
    return render(request, 'users_collections.html', context)


@login_required(login_url='login')
def create_collection(request):
    form = CollectionCreateForm()

    if request.method == 'POST':
        form = CollectionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request=request)
            return redirect('collections')

    context = {'form': form}
    return render(request, 'collection_create.html', context)


@login_required(login_url='login')
def edit_collection(request, pk):
    collection = Collection.objects.get(id=pk)
    form = CollectionEditForm(instance=collection)

    if request.user != collection.author:
        raise http.Http404  # TODO: Raise 403 Forbidden

    if request.method == 'POST':
        # TODO: Ability for editing collection cover image?
        form = CollectionEditForm(request.POST, request.FILES, instance=collection)
        if form.is_valid():
            collection = form.save()
            return redirect('collections')

    context = {'form': form}
    return render(request, 'collection_edit.html', context)


@login_required(login_url='login')
def delete_collection(request, pk):
    collection = Collection.objects.get(id=pk)

    if request.user != collection.author:
        raise http.Http404  # TODO: Return 403 Forbidden

    if request.method == 'POST':
        collection.delete()
        return redirect('collections')

    context = {'obj': f'коллекцию "{collection.name}"'}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def add_artwork_to_collection(request, pk):
    artwork_id = request.GET.get('artwork')
    artwork = get_object_or_404(Artwork, id=artwork_id)
    collection = get_object_or_404(Collection, pk=pk, author=request.user)
    art, created = CollectionArtwork.objects.get_or_create(
        collection=collection, artwork=artwork
    )
    return http.HttpResponse(status=201)


@login_required(login_url='login')
def remove_artwork_from_collection(request, pk):
    artwork_id = request.GET.get('artwork')
    artwork = get_object_or_404(Artwork, id=artwork_id)
    collection = get_object_or_404(Collection, pk=pk, author=request.user)
    try:
        art = CollectionArtwork.objects.get(collection=collection, artwork=artwork)
        art.delete()
    except CollectionArtwork.DoesNotExist:
        pass
    return http.HttpResponse(status=204)
