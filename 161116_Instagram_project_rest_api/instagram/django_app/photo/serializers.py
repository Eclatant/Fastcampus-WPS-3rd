from rest_framework import serializers

from .models import Photo, PhotoComment


class PhotoCommentSerializer(serializers.ModelSerializer):
    """
    UserSerializer를 구현하고, author field를 Nested relation으로 나타냄
    author필드에서 UserSerializer를 사용하도록 설정
    """

    class Meta:
        model = PhotoComment
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    comment_list = PhotoCommentSerializer(
        many=True,
        read_only=True,
        source=
    )

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


