from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .Views import article

urlpatterns = [
    path('articleList/', views.ArticleList.as_view(), name="article-list"),
    path('articleList/<str:categoryName>', views.ArticleList.as_view()),
    path('article/<int:pk>', views.ArticleDetail.as_view()),
    path('article/hot/', views.ArticleHotList.as_view()),
    path('article/updateNum/', article.ArticleUpdateNum.as_view()),
    path('articleLabelList/', article.ArticleLabelListView.as_view()),



    # path('article/<str:category>', views.ArticleDetail.as_view())
    # path('article', views.test, name='test'),
    # path('getArticle', views.getArticle, name='getArticle'),
    # path('article/<articleID>', views.getArticleForID, name='getArticleForID'),
    # path('articleList/<categoryName>', views.getArticleListByCategory, name='getArticleListByCategory'),
    # path('articleList/label/<labelName>', views.getArticleListByLabelName, name='getArticleListByLabelName'),
    # path('articleList/search/<keyword>', views.getSearchResult, name='getSearchResult'),
    # path('getHotArticle', articles.getHotArticle, name='getHotArticle'),
    # path('updateArticleReadNum', articles.updateArticleReadNum, name='updateArticleReadNum'),
    # path('updateArticleLikeNum', articles.updateArticleLikeNum, name='updateArticleLikeNum'),
    # path('getAllArticleLabel', articles.getAllArticleLabel, name='getAllArticleLabel'),
    # path('addUserInfo', userinfo.addUserInfo, name='addUserInfo'),
    # path('labelName', views.getArticleListByLabelName, name='getArticleListByLabelName'),
]

urlpatterns += format_suffix_patterns(urlpatterns)