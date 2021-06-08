from django.contrib import admin
from .models import Book
# Register your models here.

class BooKManager(admin.ModelAdmin):
    #列表显示哪些字段的列
    list_display = ['title','info','price']
    #控制list_display中字段 哪些可以链接到修改页
    list_display_links = ['title']
    #添加过滤器
    list_filter = ['info']
    #添加搜索框查询[模糊查询]
    search_fields = ['title']
    #添加可在列表编辑的字段
    list_editable = ['price']
admin.site.register(Book,BooKManager)