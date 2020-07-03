from django.contrib import admin
from banner.models import Banner

# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Banner._meta.fields]
    list_display.append("image_tag")
    readonly_fields = ['image_tag']
