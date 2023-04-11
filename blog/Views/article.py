import sys
import traceback

from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Article
from ..serializer import ArticleSerializer


# 更新文章的部分数量相关的数据
class ArticleUpdateNum(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def update(self, request, *args, **kwargs):
        num_type_list = ['read', 'like']
        article_id = request.data.get('id')
        article = Article.objects.get(id=article_id)
        for num_type in num_type_list:
            article_num_type = request.data.get(num_type)
            if article_num_type is not None:
                article[article_num_type] += 1
                article.save()
        return Response({
            'status': 'success',
            'responseCode': status.HTTP_200_OK,
        })


# 获取所有标签列表
class ArticleLabelListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        # 加上flat=True参数，可以让返回的queryset的成员为单个值而非元组
        labels = Article.objects.values_list('label', flat=True)
        # 去掉其中的逗号并拼接为一个数组
        labels = [label.split(',') for label in labels]
        labels = [item for sublist in labels for item in sublist]
        # 去重
        labels = list(set(labels))
        return Response({
            'status': 'success',
            'responseCode': status.HTTP_200_OK,
            'data': labels
        })


# 获取热门文章
# def getHotArticle(request):
#     responseList = []
#     try:
#         articleTitle = article.objects.filter(readNum__gte=0)
#         for i in articleTitle:
#             responseList.append(model_to_dict(i))
#     except Exception as e:
#         GetErrorInfo()
#
#     return JsonResponse(responseList, safe=False)
#
#
# # 更新文章阅读数
# def updateArticleReadNum(request):
#     # responseList = []
#     try:
#         # 将非表单数据转换成字典对象
#         requestData = json.loads(request.body)
#         resultObj = article.objects.get(id=requestData.get('id'))
#         resultObj.readNum += 1
#         resultObj.save()
#     except Exception as e:
#         GetErrorInfo()
#     return JsonResponse({'result': 'success'}, safe=False)
#
#
# # 更新文章点赞数
# def updateArticleLikeNum(request):
#     try:
#         # 将非表单数据转换成字典对象
#         requestData = json.loads(request.body)
#         resultObj = article.objects.get(id=requestData.get('id'))
#         resultObj.likeNum += 1
#         resultObj.save()
#     except Exception as e:
#         GetErrorInfo()
#     return JsonResponse({'result': 'success'}, safe=False)
#
#
# # 取出所有文章的标签，并返回给前端处理后的标签列表
# def getAllArticleLabel(request):
#     responseList = []  # 要返回的数据
#     tempList = []
#     try:
#         labelList = article.objects.values_list('label', flat=True)
#         for i in labelList:
#             tempList.append(i)
#         for i in tempList:
#             splitList = i.split(',')
#             for j in splitList:
#                 responseList.append(j)
#         # 去重
#         responseList = list(set(responseList))
#     except Exception as e:
#         GetErrorInfo()
#     return JsonResponse({"status": "success", "data": responseList}, safe=False)


# 输出错误信息
def GetErrorInfo():
    exc_type, exc_value, exc_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_obj, limit=2, file=sys.stdout)
