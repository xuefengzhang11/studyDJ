from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
    path('hotArticle/', views.hotArticle, name='hotArticle'),  # 得到热门文章
    url(r'getArticleById/(?P<id>\d+)/(?P<tel>\w*)/', views.getArticleById, name='getArticleById'),  # 根据ID得到文章信息

    url(r'^acountArticle\w*/(?P<con>\w*)/', views.acount, name='acount'),  # 求文章总数
    url(r'^getArticle/(?P<pageIndex>\d*)/(?P<con>\w*)/', views.getArticle, name='getArticle'),  # 得到文章
    url(r'^getUserArticle/(?P<id>\d+)', views.getUserArticle, name='getUserArticle'),
    url(r'^getCollectArticle/(?P<tel>\d+)', views.getCollectArticle, name='getCollectArticle'),  # 根据tel获取已经收藏的文章
    url(r'^getMyArticle/(?P<tel>\d+)', views.getMyArticle, name='getMyArticle'),  # 根据tel获取我的文章
    url(r'getComment/(?P<artid>\d+)/(?P<usertel>\d*)', views.getComment, name='getComment'), # 通过文章ID获取文章所有评论
    url(r'deleteArticle/(?P<id>\w*)', views.deleteArticle, name='deleteArticle'),  # 删除收藏文章
    url(r'deleteUserArticle/(?P<id>\w*)', views.deleteUserArticle, name='deleteUserArticle'),  # 删除个人文章
    url(r'insertArticleLike/(?P<articleid>\w*)/(?P<tel>\d+)', views.insertArticleLike, name='insertArticleLike'),  # 添加文章点赞
    url(r'deteleArticleLike/(?P<articleid>\w*)/(?P<tel>\d+)', views.deteleArticleLike, name='deteleArticleLike'),  # 删除文章点赞
    url(r'insertCommentLike/(?P<commid>\w*)/(?P<tel>\d+)', views.insertCommentLike, name='insertCommentLike'),  # 添加或者删除评论点赞
    url(r'insertReplyLike/(?P<replyid>\w*)/(?P<tel>\d+)', views.insertReplyLike, name='insertReplyLike'),  # 添加或者删除评论评论点赞
    url(r'insertArticleCommet/', views.insertArticleCommet, name='insertArticleCommet'),  # 添加文章评论内容
    url(r'insertCommentContent/', views.insertCommentContent, name='insertCommentContent'),  # 添加评论回复内容
]
