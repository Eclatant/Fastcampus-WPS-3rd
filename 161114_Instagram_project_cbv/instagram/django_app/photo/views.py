from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'photo_list.html', context)


class PhotoList(ListView):
    model = Photo
    paginate_by = 3
    context_object_name = 'photos'
    # queryset = Photo.objects.filter(created_date__year__gt=2015)


class PhotoAdd(CreateView):
    model = Photo
    fields = ['image', 'content']
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoAdd, self).form_valid(form)
