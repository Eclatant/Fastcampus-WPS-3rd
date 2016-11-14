from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Photo, PhotoComment


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


class PhotoCommentAdd(CreateView):
    model = PhotoComment
    fields = ['content']

    

class PhotoDetail(View):
    """
    1. PhotoDisplay(DetailView)를 구현
    2. PhotoDetail의 get에 연결
    3. PhotoCommentAdd(CreateView) 구현
    4. PhotoDetail의 post에 연결
    """
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


@method_decorator(login_required, name='dispatch')
class PhotoAdd(CreateView):
    model = Photo
    fields = ['image', 'content']
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoAdd, self).form_valid(form)
