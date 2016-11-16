import json

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from photo.serializers import PhotoSerializer
from .models import Photo, PhotoComment

User = get_user_model()


class PhotoList(APIView):
    csrf_exempt = True
    
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def photo_list(request):
    photos = Photo.objects.all()
    data = {
        'photos': [photo.to_dict() for photo in photos],
    }
    return HttpResponse(
        json.dumps(data),
        content_type='application/json'
    )


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
    return HttpResponse(
        json.dumps(photo.to_dict()),
        content_type='application/json'
    )


@csrf_exempt
def comment_add(request, photo_pk):
    data = request.POST

    user_id = data['user_id']
    content = data['content']

    author = User.objects.get(id=user_id)
    photo = Photo.objects.get(id=photo_pk)

    photo_comment = PhotoComment.objects.create(
        photo=photo,
        author=author,
        content=content
    )
    return HttpResponse(
        json.dumps(photo_comment.to_dict()),
        content_type='application/json'
    )