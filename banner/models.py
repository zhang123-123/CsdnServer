from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Banner(models.Model):
    banner_src = models.ImageField(upload_to="static/imgs/banner", null=True, blank=True, verbose_name="轮播图片")
    banner_level = models.IntegerField(default=0, verbose_name="图片优先级")
    banner_url = models.CharField(max_length=255, verbose_name="轮播详情")

    def image_tag(self):
        return mark_safe('<img src="http://127.0.0.1:8000/{}" width="150" height="150"/>'.format(self.banner_src.url))

    image_tag.short_description = '轮播图片'

    class Meta:
        db_table = "banner"
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name