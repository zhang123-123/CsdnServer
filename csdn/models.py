from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class CsdnBlog(models.Model):
    user_img = models.ImageField(upload_to="static/imgs/csdnblog", null=True, blank=True, verbose_name="用户头像")
    user_name = models.CharField(max_length=255, verbose_name="博客发布人", null=True, blank=True)
    blog_title = models.CharField(max_length=255, verbose_name="博客标题", null=True, blank=True)
    blog_url = models.CharField(max_length=255, verbose_name="博客原文链接", null=True, blank=True)
    blog_intro = models.TextField(verbose_name="博客简介", null=True, blank=True)
    blog_content = models.TextField(verbose_name="博客内容", null=True, blank=True)
    blog = models.ForeignKey('BlogType', on_delete=models.DO_NOTHING, verbose_name="博客类别id", null=True, blank=True)
    zan = models.IntegerField(default=0, verbose_name="点赞人数")
    liulan = models.IntegerField(default=0, verbose_name="浏览人数")
    blog_time = models.DateTimeField(verbose_name="博客发布日期", null=True, blank=True)

    # def image_tag(self):
    #     return mark_safe('<img src="http://127.0.0.1:8000/{}" width="150" height="150"/>'.format(self.user_img.url))
    #
    # image_tag.short_description = '用户头像'

    class Meta:
        db_table = "csdnblog"
        verbose_name = "csdn博客"
        verbose_name_plural = verbose_name


class ZanCsdnBlog(models.Model):
    user_name = models.CharField(max_length=255, verbose_name="点赞人", null=True, blank=True)
    blog_id = models.IntegerField(default=0, verbose_name="博客id", null=True, blank=True)
    zan_status = models.BooleanField(default=False, verbose_name="点赞状态")

    class Meta:
        db_table = "zancsdnblog"
        verbose_name = "点赞状态表"
        verbose_name_plural = verbose_name


class BlogType(models.Model):
    blog_type = models.CharField(max_length=255, verbose_name="博客类型名", null=True, blank=True)

    class Meta:
        db_table = "blogtype"
        verbose_name = "博客分类表"
        verbose_name_plural = verbose_name



class LiuLanCsdnBlog(models.Model):
    user_name = models.CharField(max_length=255, verbose_name="浏览人", null=True, blank=True)
    blog = models.ForeignKey("CsdnBlog", on_delete=models.DO_NOTHING, verbose_name="博客id", null=True, blank=True)
    liulan_time = models.DateTimeField(auto_now_add=True, verbose_name="浏览时间", null=True, blank=True)

    class Meta:
        db_table = "liulancsdnblog"
        verbose_name = "浏览表"
        verbose_name_plural = verbose_name
