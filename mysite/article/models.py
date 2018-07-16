from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from slugify import  slugify
from django.core.urlresolvers import reverse

class ArticleColumn(models.Model):
    """文章栏目"""
    user = models.ForeignKey(User,related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

class ArticleTag(models.Model):
    author = models.ForeignKey(User,related_name="tag")
    tag = models.CharField(max_length=500)

    def __str__(self):
        return self.tag

class ArticlePost(models.Model):
    """文章信息"""
    author = models.ForeignKey(User,related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn,related_name="article_column")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User, related_name="articles_like", blank=True)
    article_tag = models.ManyToManyField(ArticleTag,related_name="article_tag",blank=True)

    class Meta:
        ordering = ("title",)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(ArticlePost,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("article:article_detail",args=[self.id,self.slug])

    def get_url_path(self):
        return reverse("article:list_article_detail",args=[self.id,self.slug])


class Comment(models.Model):
    article = models.ForeignKey(ArticlePost,related_name="comments")#通过ForeignKey将本数据模型与ArticlePost建立关系
    commentator = models.CharField(max_length=90)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",) #此处用的是元组类型，不要丢掉后面的逗号，负号意味着按照字段的倒序

    def __str__(self):
        return "Comment by {0} on {1}".format(self.commentator.username, self.article)

