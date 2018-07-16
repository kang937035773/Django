#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @author: 胡晓康
  @file: forms.py 
  @time: 2018/7/3 20:53
  @desc:
  """
from  django import forms
from .models import ArticleColumn,ArticlePost,Comment,ArticleTag

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields=("column",)

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ("title","body")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("commentator","body",)

class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = ArticleTag
        fields = ('tag',)