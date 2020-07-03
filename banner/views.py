from django.shortcuts import render
from django.http import JsonResponse
from banner.models import Banner
from rest_framework.views import APIView


# Create your views here.
class BannerView(APIView):
    def get(self, request, *args, **kwargs):
        result = {}
        banners = Banner.objects.all()
        if banners:
            result["code"] = "001"
            result["message"] = "查询成功"
            result["datas"] = []
            for banner in banners:
                a = {}
                a["banner_src"] = banner.banner_src.url
                a["banner_level"] = banner.banner_level
                a["banner_url"] = banner.banner_url
                result["datas"].append(a)
        else:
            result["code"] = "002"
            result["message"] = "没有查询到数据"
        return JsonResponse(result)

#
# def BannerView1(request):
#     if request.method == "GET":
#         result = {}
#         banners = Banner.objects.all()
#         if banners:
#             result["code"] = "001"
#             result["message"] = "查询成功"
#             result["datas"] = []
#             for banner in banners:
#                 a = {}
#                 a["banner_src"] = banner.banner_src.url
#                 a["banner_level"] = banner.banner_level
#                 a["banner_url"] = banner.banner_url
#                 result["datas"].append(a)
#         else:
#             result["code"] = "002"
#             result["message"] = "没有查询到数据"
#         return JsonResponse(result)
