from django.urls import path
from . import views
from .Articles import article as articles
from .Views import userinfo
urlpatterns = [
    path('article', views.test, name='test'),
    path('getArticle', views.getArticle, name='getArticle'),
    path('article/<articleID>', views.getArticleForID, name='getArticleForID'),
    path('articleList/<categoryName>', views.getArticleListByCategory, name='getArticleListByCategory'),
    path('articleList/label/<labelName>', views.getArticleListByLabelName, name='getArticleListByLabelName'),
    path('articleList/search/<keyword>', views.getSearchResult, name='getSearchResult'),
    path('getHotArticle', articles.getHotArticle, name='getHotArticle'),
    path('updateArticleReadNum', articles.updateArticleReadNum, name='updateArticleReadNum'),
    path('updateArticleLikeNum', articles.updateArticleLikeNum, name='updateArticleLikeNum'),
    path('getAllArticleLabel', articles.getAllArticleLabel, name='getAllArticleLabel'),
    path('addUserInfo', userinfo.addUserInfo, name='addUserInfo'),
    # path('labelName', views.getArticleListByLabelName, name='getArticleListByLabelName'),
]