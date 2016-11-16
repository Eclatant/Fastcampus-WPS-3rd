from rest_framework import serializers

from .models import Photo, PhotoComment


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation()
        ret['commentList'] = PhotoCommentSerializer(
            data=instance.photocomment_set.all(),
            many=True).data
        return ret


class PhotoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = '__all__'