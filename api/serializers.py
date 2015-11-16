from django.contrib.auth.models import User
from rest_framework import serializers
from chirp.models import Chirp, Favorite


class UserSerializer(serializers.HyperlinkedModelSerializer):
    chirp_set = serializers.\
        HyperlinkedRelatedField(many=True, queryset=Chirp.objects.all(),
                                view_name='api_chirp_detail_update')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'chirp_set')


class ChirpSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    favorite_set = serializers.StringRelatedField(many=True, read_only=True)
    favorite_users = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Chirp
        fields = ('id', 'author', 'message', 'title', 'posted_at',
                  'favorite_set', 'favorite_users')

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'chirp', 'favorited_att')
