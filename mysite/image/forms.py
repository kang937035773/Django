#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @author: 胡晓康
  @file: forms.py 
  @time: 2018/7/12 14:49
  @desc:
  """
from django import forms
from django.core.files.base import ContentFile
from slugify import slugify
from urllib import request

from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url', 'description')

    def clean_url(self):
        url = self.cleaned_data['url']#获取相应字段的值
        valid_extensions = ['jpg', 'jpeg', 'png']#规定了图片的扩展名
        extension = url.rsplit('.',1)[1].lower() #从得到的图片的网址中分解出其扩展名
        if extension not in valid_extensions:
            raise forms.ValidationError("The given Url does not match valid image extension.")
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{0}.{1}'.format(slugify(image.title), image_url.rsplit('.', 1)[1].lower())
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()

        return image