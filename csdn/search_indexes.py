# -*- coding:utf-8 -*-

from haystack import indexes
from .models import CsdnBlog


class CsdnBlogIndex(indexes.SearchIndex, indexes.Indexable):
    # 类名必须为需要检索的Model_name+Index，
    # 这里需要检索Specification，所以创建SpecificationIndex
    text = indexes.CharField(document=True, use_template=True, template_name='CsdnBlog_text.txt')

    def get_model(self):  # 重载get_model方法，必须要有！
        return CsdnBlog

    def index_queryset(self, using=None):  # 重载index_queryset函数
        return self.get_model().objects.all()
