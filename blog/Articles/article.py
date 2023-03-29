import sys
import traceback
import json

from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ..models import *


# 获取热门文章
def getHotArticle(request):
    responseList = []
    try:
        articleTitle = article.objects.filter(readNum__gte=0)
        for i in articleTitle:
            responseList.append(model_to_dict(i))
    except Exception as e:
        GetErrorInfo()

    return JsonResponse(responseList, safe=False)


# 更新文章阅读数
def updateArticleReadNum(request):
    # responseList = []
    try:
        # 将非表单数据转换成字典对象
        requestData = json.loads(request.body)
        resultObj = article.objects.get(id=requestData.get('id'))
        resultObj.readNum += 1
        resultObj.save()
    except Exception as e:
        GetErrorInfo()
    return JsonResponse({'result': 'success'}, safe=False)


# 更新文章点赞数
def updateArticleLikeNum(request):
    try:
        # 将非表单数据转换成字典对象
        requestData = json.loads(request.body)
        resultObj = article.objects.get(id=requestData.get('id'))
        resultObj.likeNum += 1
        resultObj.save()
    except Exception as e:
        GetErrorInfo()
    return JsonResponse({'result': 'success'}, safe=False)


# 取出所有文章的标签，并返回给前端处理后的标签列表
def getAllArticleLabel(request):
    responseList = []  # 要返回的数据
    tempList = []
    try:
        labelList = article.objects.values_list('label', flat=True)
        for i in labelList:
            tempList.append(i)
        for i in tempList:
            splitList = i.split(',')
            for j in splitList:
                responseList.append(j)
        # 去重
        responseList = list(set(responseList))
    except Exception as e:
        GetErrorInfo()
    return JsonResponse({"status": "success", "data": responseList}, safe=False)


# 输出错误信息
def GetErrorInfo():
    exc_type, exc_value, exc_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_obj, limit=2, file=sys.stdout)
