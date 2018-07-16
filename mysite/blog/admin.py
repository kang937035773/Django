from django.contrib import admin
from .models import BlogArticles
# Register your models here.
class BlogArticlesAdmin(admin.ModelAdmin):
    #页面显示的字段
    list_display = ("title","author","publish")
    #按照指定的字段来排序
    list_filter = ("publish","author")
    #添加一个搜索框，可以按照给的字段进行搜索
    search_fields = ("title","body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish','author']


admin.site.register(BlogArticles,BlogArticlesAdmin)
