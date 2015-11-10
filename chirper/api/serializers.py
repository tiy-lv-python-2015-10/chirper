from django.contrib.auth.models import User
from rest_framework import serializers
from chirp.models import Chirp

class UserSerializer(serializers.HyperlinkedModelSerializer):
    chirp_set = serializers.HyperlinkedRelatedField(many=True,
                                                    queryset=Chirp.objects.all(),
                                                    view_name='api_chirp_detail_update')
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'chirp_set')


class ChirpSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Chirp
        fields = ('id', 'author', 'message', 'title', 'posted_at')