from rest_framework import serializers

from .models import MatchDetails


class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDetails
        fields = ('match_id', 'response')
