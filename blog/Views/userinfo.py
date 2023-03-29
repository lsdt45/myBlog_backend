import sys
import traceback
import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import *
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from ..serializer import UserInfoSerializer
from rest_framework.views import APIView


class UserInfoView(ListCreateAPIView, RetrieveDestroyAPIView):
    serializer_class = UserInfoSerializer
    # 使用article模型中的所有数据
    queryset = userInfo.objects.all()
    # 仅允许认证用户的读写操作
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def addUserInfo(self, request):
        response = []
        try:
            requestDic = json.loads(request.body)
            user = userInfo(ip=requestDic.get('ip'), ad_info=requestDic.get('ad_info'))
            # userInfo.objects.create(ip=requestDic.get('ip'), ad_info=requestDic.get('ad_info'))
            user.save()
        except Exception as e:
            GetErrorInfo()
        return JsonResponse({"status": "success"}, safe=False)


# 输出错误信息
def GetErrorInfo():
    exc_type, exc_value, exc_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_obj, limit=2, file=sys.stdout)
