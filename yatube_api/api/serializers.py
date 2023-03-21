from rest_framework import serializers

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('created', 'post')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    group = serializers.SlugRelatedField(
        read_only=True, slug_field='title'
    )

    class Meta:
        fields = ('id', 'text', 'image', 'group', 'author', 'pub_date')
        read_only_fields = ('pub_date',)
        model = Post
