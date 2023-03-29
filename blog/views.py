import sys
import traceback
import json

from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import generics
from .models import article


# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()

# 获取文章列表
def getArticle(request):
    responseList = []
    try:
        articleTitle = article.objects.filter()
        for i in articleTitle:
            responseList.append(model_to_dict(i))
    except Exception as e:
        GetErrorInfo()

    return JsonResponse(responseList, safe=False)


# 通过ID获取文章内容
def getArticleForID(request, articleID):
    responseList = []
    try:
        articleData = article.objects.filter(id=articleID)
        for i in articleData:
            responseList.append(model_to_dict(i))
    except Exception as e:
        GetErrorInfo()

    return JsonResponse(responseList, safe=False)


# 通过类型获取文章列表
def getArticleListByCategory(request, categoryName):
    responseList = []
    try:
        articleData = article.objects.filter(category=categoryName)
        for i in articleData:
            responseList.append(model_to_dict(i))

    except Exception as e:
        GetErrorInfo()

    return JsonResponse(responseList, safe=False)


# 通过标签名获取文章列表
def getArticleListByLabelName(request, labelName):
    responseList = []
    try:
        articleData = article.objects.filter(label__contains=labelName)
        for i in articleData:
            responseList.append(model_to_dict(i))

    except Exception as e:
        GetErrorInfo()

    return JsonResponse(responseList, safe=False)


# 获取搜索结果
def getSearchResult(request, keyword):
    responseList = []

    try:
        # 从title和content中检索符合条件的article
        articleData_title = article.objects.filter(title__contains=keyword)
        articleData_content = article.objects.filter(content__contains=keyword)
        for i in articleData_title:
            responseList.append(model_to_dict(i))

        # 去重
        for i in articleData_content:
            flag = True
            for j in responseList:
                if i.title == j['title']:
                    flag = False
                    break
            if flag is True:
                responseList.append(model_to_dict(i))

    except Exception as e:
        GetErrorInfo()

    return JsonResponse(responseList, safe=False)


# 输出错误信息
def GetErrorInfo():
    exc_type, exc_value, exc_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_obj, limit=2, file=sys.stdout)
