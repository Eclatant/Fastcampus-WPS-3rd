from django.shortcuts import redirect, render, get_object_or_404
from ..models import Album, Photo, PhotoLike, PhotoDislike
from ..forms import PhotoForm

__all__ = [
    'photo_add',
]


def photo_add(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            # img = request.FILES['img']
            img = form.cleaned_data['img']
            Photo.objects.create(
                album=album,
                owner=request.user,
                title=title,
                description=description,
                img=img,
            )
            return redirect('photo:album_detail', pk=album_pk)
    else:
        form = PhotoForm()
    context = {
        'form': form,
    }
    return render(request, 'photo/photo_add.html', context)