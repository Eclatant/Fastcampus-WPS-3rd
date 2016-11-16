from rest_framework import serializers

from .models import Photo, PhotoComment


class PhotoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    photocomment_set = PhotoCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Photo
        fields = (
            'id',
            'author',
            'content',
            'image',
            'photocomment_set',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # ret['comment_list'] = PhotoCommentSerializer(
        #     instance.photocomment_set.all(),
        #     many=True).data
        return ret


