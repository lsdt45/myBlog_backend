from rest_framework import serializers
from .models import userInfo, Article


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userInfo
        fields = ('ip', 'ad_info')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "id", "title", "Introduction", "category", "label", "content", "likeNum", "comment", "commentNum",
            "addDate", "modifyDate", "readNum", "coverPath")
