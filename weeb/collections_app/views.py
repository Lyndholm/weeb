from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CollectionCreateForm


@login_required(login_url='login')
def create_collection(request):
    form = CollectionCreateForm()

    if request.method == 'POST':
        form = CollectionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request=request)
            return redirect('home')

    context = {'form': form}
    return render(request, 'collection_create.html', context)
