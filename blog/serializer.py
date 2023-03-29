from rest_framework import serializers
from .models import userInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userInfo
        fields = ('ip', 'ad_info')
