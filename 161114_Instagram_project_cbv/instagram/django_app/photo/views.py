from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import SingleObjectMixin, DetailView

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

    def form_valid(self, form):
        photo_pk = self.kwargs.get('photo_pk')
        photo = get_object_or_404(Photo, photo_pk)
        form.instance.photo = photo
        form.instance.author = self.request.user
        return super(PhotoCommentAdd, self).form_valid(form)


class PhotoDisplayView(DetailView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PhotoCommentForm()
        return context


class PhotoCommentForm(forms.Form):
    content = forms.CharField()


class PhotoCommentFormView(SingleObjectMixin, FormView):
    template_name = 'photo/photo_detail.html'
    form_class = PhotoCommentForm
    model = Photo

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(PhotoCommentFormView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        content = form.cleaned_data['content']
        print(content)

    def get_success_url(self):
        return reverse('photo:photo_detail', kwargs={'pk': self.object.pk})


class PhotoDetail(View):
    """
    1. PhotoDisplay(DetailView)를 구현
    2. PhotoDetail의 get에 연결
    3. PhotoCommentAdd(CreateView) 구현
    4. PhotoDetail의 post에 연결
    """
    def get(self, request, *args, **kwargs):
        view = PhotoDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PhotoCommentFormView.as_view()
        return view(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class PhotoAdd(CreateView):
    model = Photo
    fields = ['image', 'content']
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoAdd, self).form_valid(form)
