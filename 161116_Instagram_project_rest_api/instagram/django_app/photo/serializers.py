from rest_framework import serializers

from .models import Photo, PhotoComment


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'id',
            'author',
            'content',
            'image',
            'comment_set',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # ret['comment_list'] = PhotoCommentSerializer(
        #     instance.photocomment_set.all(),
        #     many=True).data
        return ret


class PhotoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = '__all__'