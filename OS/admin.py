# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from OS.models import TClass, TGroup, TJob, TStudent, TSubject, TTeacher


class OsModel(admin.ModelAdmin):
    list_display = []
    # # 查询框查询字段
    # list_filter = ("title", "created",)
    # # 站内查询，搜索框，根据某些字段查询（精细、模糊均可）
    # search_fields = ("id", "desc", "content", "category", "title",)


admin.site.register(TClass)
admin.site.register(TGroup)
admin.site.register(TJob)
admin.site.register(TStudent)
admin.site.register(TSubject)
admin.site.register(TTeacher)