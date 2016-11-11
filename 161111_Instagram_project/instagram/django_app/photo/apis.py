from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .models import Photo
User = get_user_model()


@csrf_exempt
def photo_add(request):
    data = request.POST
    files = request.FILES

    user_id = data['user_id']
    content = data['content']
    image = files['photo']

    author = User.objects.get(id=user_id)
    photo = Photo.objects.create(
        image=image,
        author=author,
        content=content
    )