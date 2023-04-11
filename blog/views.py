import sys
import traceback
import json

from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import generics
from .models import Article
from .serializer import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # fields = ["category", "label"]
        fields = ["label"]
        category = self.kwargs.get('categoryName')
        if category is not None:
            queryset = Article.objects.filter(category=category)

        for field in fields:
            value = self.request.query_params.get(field, None)
            if value is not None:
                if value == "any":
                    # f-string语法：在字符串前面加一个f，然后在字符串中用大括号 { } 包含要替换的表达式或变量。Python会在运行时计算这些表达式或变量的值，并替换到字符串中。
                    # __regex是一个字段查找方法，它表示要用正则表达式来匹配字段的值。r"."是一个正则表达式，它表示匹配任何非空字符。
                    # f"{field}__regex": r"." 的意思是，用正则表达式r"."来匹配field字段的值。这相当于查询任何非空值。
                    # “**”表示字典解包，作用是将一个字典作为关键字传递给一个函数。
                    queryset = queryset.filter(**{f"{field}__regex": r"."})
                else:
                    # 加上__contain，以模糊匹配
                    queryset = queryset.filter(**{field + '__contains': value})

        return queryset


# 返回阅读数前4的文章列表
class ArticleHotList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.order_by('-readNum')[:4]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# 输出错误信息
def GetErrorInfo():
    exc_type, exc_value, exc_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_obj, limit=2, file=sys.stdout)
