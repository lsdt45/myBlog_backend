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

class UserInfoView(ListCreateAPIView, RetrieveDestroyAPIView):
    serializer_class = UserInfoSerializer
    # 使用userInfo模型中的所有数据
    queryset = userInfo.objects.all()




# 输出错误信息
def GetErrorInfo():
    exc_type, exc_value, exc_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_obj, limit=2, file=sys.stdout)
