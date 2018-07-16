from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#文章模型
class BlogArticles(models.Model):
    title = models.CharField(max_length = 300)
    #一个用户对应多个文章，ForeignKey()就反映了这种“一对多的”关系
    #related_name='blog_posts'的作用是允许通过类User
    #反向查询到BlogArticle
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)

    class Meta:
        #规定了BlogArticle实例对象的显示顺序，在这里使按照publish的倒序显示
        ordering=('-publish',)

    def __str__(self):
        return self.title
