#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @author: 胡晓康
  @file: urls.py 
  @time: 2018/7/3 21:12
  @desc:
  """
from django.conf.urls import url,include
from . import views,list_views

urlpatterns = [
    url(r'^article-column/$',views.article_column,name="article_column"),
    url(r'^rename-article-column/$',views.rename_article_column,name="rename_article_column"),
    url(r'^delete-article-column/$',views.delete_article_column,name="delete_article_column"),
    url(r'^article-post/$',views.article_post,name="article_post"),
    url(r'^article-list/$',views.article_list,name="article_list"),
    url(r'^article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name="article_detail"),
    url(r'^del-article/$', views.del_article, name="del_article"),
    url(r'^redit-article/(?P<article_id>\d+)/$', views.redit_article, name="redit_article"),
    url(r'^list-article-titles/$', list_views.article_titles, name="article_titles"),
    url(r'^list-article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', list_views.article_detail, name="list_article_detail"),
    url(r'^list-article-titles/(?P<username>[-\w]+)/$',list_views.article_titles,name="author_articles"),
    url(r'^like-article/$',list_views.like_article,name="like_article"),
    url(r'^article-tag/$',views.article_tag,name="article_tag"),
    url(r'^del-article-tag/$',views.del_article_tag,name="del_article_tag"),
]
