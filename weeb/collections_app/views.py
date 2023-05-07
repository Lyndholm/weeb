from artworks.views import paginate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CollectionCreateForm
from .models import Collection


def collections_home_page(request):
    collections = Collection.objects.all()
    collections = paginate(request, collections, 10)

    context = {'collections': collections}
    return render(request, 'collections.html', context)


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
