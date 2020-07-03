# -*- coding:utf-8 -*-
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import CsdnBlog, ZanCsdnBlog, BlogType, LiuLanCsdnBlog
from tools import orm2json
import time
from tools.time_data import time_
from tools.gjz_h import my_highlight
# from tools.gjz_hi import my_highlight
from haystack.views import SearchView


# Create your views here.
class CsdnBlogView(APIView):
    def get(self, request, *args, **kwargs):
        result = {}
        username = request.GET.get("user_name")
        blog_id = request.GET.get("blog_id")
        print(username, blog_id)
        if blog_id:
            # 根据博客id获取博客信息
            csdnblogs = CsdnBlog.objects.filter(id=blog_id)
            if csdnblogs:
                csdnblog = csdnblogs[0]
                result["cdde"] = "001"
                result["message"] = "查询成功"
                result["blog_info"] = {}
                result["blog_info"]["user_name"] = csdnblog.user_name
                result["blog_info"]["id"] = csdnblog.id
                result["blog_info"]["blog_content"] = csdnblog.blog_content.replace('src="csdn图片/imgs',
                                                                                    r'src="http://115.29.150.206:8001/static/csdn_imgs')
                blogtypes = BlogType.objects.filter(id=csdnblog.blog.id)
                if blogtypes:
                    blogtype = blogtypes[0]
                    blogtypename = blogtype.blog_type
                else:
                    blogtypename = ""

                result["blog_info"]["blog_type"] = blogtypename
                result["blog_info"]["zan"] = csdnblog.zan
                result["blog_info"]["liulan"] = csdnblog.liulan
                result["blog_info"]["blog_time"] = csdnblog.blog_time
                result["blog_info"]["blog_title"] = csdnblog.blog_title
                result["blog_info"]["blog_url"] = csdnblog.blog_url
                zancsdnblogs = ZanCsdnBlog.objects.filter(Q(blog_id=csdnblog.id) & Q(user_name=username)).order_by(
                    "-id")
                if zancsdnblogs:
                    zancsdnblog = zancsdnblogs[0]
                    is_true = zancsdnblog.zan_status
                    if is_true:
                        a = "true"
                    else:
                        a = "false"
                else:
                    a = "false"
                result["blog_info"]["zan_status"] = a
                csdnblog.liulan += 1
                csdnblog.save()
                ll_blog = LiuLanCsdnBlog()
                ll_blog.user_name = username
                ll_blog.blog = csdnblog
                ll_blog.save()
        else:
            # print(username)

            csdnblogs = CsdnBlog.objects.all().order_by("-blog_time")[:10]
            if csdnblogs:
                result["code"] = "001"
                result["message"] = "查询成功"
                result["datas"] = []
                for csdnblog in csdnblogs:
                    a = {}
                    # a["user_img"] = csdnblog.user_img
                    a["user_name"] = csdnblog.user_name
                    a["id"] = csdnblog.id
                    a["blog_intro"] = csdnblog.blog_intro
                    a["blog_content"] = csdnblog.blog_content
                    blogtypes = BlogType.objects.filter(id=csdnblog.blog.id)
                    if blogtypes:
                        blogtype = blogtypes[0]
                        blogtypename = blogtype.blog_type
                    else:
                        blogtypename = ""
                    a["blog_type"] = blogtypename
                    a["zan"] = csdnblog.zan
                    a["liulan"] = csdnblog.liulan
                    a["blog_time"] = csdnblog.blog_time
                    a["blog_title"] = csdnblog.blog_title
                    zancsdnblogs = ZanCsdnBlog.objects.filter(Q(blog_id=csdnblog.id) & Q(user_name=username)).order_by(
                        "-id")
                    if zancsdnblogs:
                        zancsdnblog = zancsdnblogs[0]
                        is_true = zancsdnblog.zan_status
                        if is_true:
                            a["zan_status"] = "true"
                        else:
                            a["zan_status"] = "false"
                    else:
                        a["zan_status"] = "false"
                    result["datas"].append(a)
            else:
                result["code"] = "002"
                result["message"] = "没有查询到数据"
        return JsonResponse(result)

    def post(self, request, *args, **kwargs):
        result = {}
        id = request.POST.get("id")
        user_name = request.POST.get("user_name")
        is_zan = request.POST.get("is_zan")
        print(id, user_name, is_zan, type(is_zan))
        csdnblogs = CsdnBlog.objects.filter(id=id)
        if csdnblogs:
            csdnblog = csdnblogs[0]
            zancsdnblog = ZanCsdnBlog()
            zancsdnblog.user_name = user_name
            zancsdnblog.blog_id = id

            result["datas"] = []
            a = {}
            if is_zan == "true":
                result["code"] = "001"
                result["message"] = "点赞成功"
                csdnblog.zan += 1
                zancsdnblog.zan_status = True
            elif is_zan == "false":
                result["code"] = "001"
                result["message"] = "取消点赞"
                if csdnblog.zan > 1:
                    csdnblog.zan -= 1
                zancsdnblog.zan_status = False
            a["zan"] = csdnblog.zan
            result["zan_num"] = csdnblog.zan
            zancsdnblog.save()
            csdnblog.save()


        else:
            result["code"] = "002"
            result["message"] = "点赞失败"
        return JsonResponse(result)


# 获取博客类型
class TypeView(APIView):
    def get(self, request, *args, **kwargs):
        result = {}
        blog_types = BlogType.objects.all()
        result["code"] = "001"
        result["message"] = "查询成功"
        result["blog_type"] = [
            {
                "blog_type_id": -2,
                "blog_type_name": "全部",
            },
            {
                "blog_type_id": -1,
                "blog_type_name": "推荐",
            },
        ]
        for blog_type in blog_types:
            a = {}
            a["blog_type_id"] = blog_type.id
            a["blog_type_name"] = blog_type.blog_type
            result["blog_type"].append(a)
        return JsonResponse(result)


# 根据博客类型获取博客数据
class BlogTypeView(APIView):
    def get(self, request, *args, **kwargs):
        # blog_types = BlogType.objects.all()
        user_name = request.GET.get("user_name", "1  2  3")
        blog_type_id = request.GET.get("blog_type_id", -2)
        page = request.GET.get("page", 1)
        pagesize = request.GET.get("pagesize", 15)
        blog_type_id = int(blog_type_id)
        page = int(page)
        pagesize = int(pagesize)
        print(user_name, blog_type_id, page, blog_type_id)
        result = {}
        """
        result = {
            "code":"",
            "message": "",
            "all_blog": [{}, {}],
            "tuijian_blog": [{}, {}],
            "data": [{"":[{}, {}]},{"":[{}, {}]}]
        }
        """
        result["code"] = "001"
        result["message"] = "查询成功"
        result["all_blog"] = []
        result["tuijian_blog"] = []
        result["type_blogs"] = []
        result["blogs"] = []
        if blog_type_id == -2:
            all_csdnblogs = CsdnBlog.objects.raw(
                f"""select * from csdnblog LEFT JOIN blogtype on csdnblog.blog_id=blogtype.id ;""")[
                            (page - 1) * pagesize: page * pagesize]
            for all_csdnblog in all_csdnblogs:
                a = {}
                a["user_name"] = all_csdnblog.user_name
                a["id"] = all_csdnblog.id
                a["blog_intro"] = all_csdnblog.blog_intro
                # a["blog_content"] = all_csdnblog.blog_content
                a["blog_type"] = all_csdnblog.blog_type
                a["zan"] = all_csdnblog.zan
                a["liulan"] = all_csdnblog.liulan
                a["blog_time"] = all_csdnblog.blog_time
                a["blog_title"] = all_csdnblog.blog_title
                zancsdnblogs = ZanCsdnBlog.objects.filter(Q(blog_id=all_csdnblog.id) & Q(user_name=user_name)).order_by(
                    "-id")
                if zancsdnblogs:
                    zancsdnblog = zancsdnblogs[0]
                    is_true = zancsdnblog.zan_status
                    if is_true:
                        a["zan_status"] = "true"
                    else:
                        a["zan_status"] = "false"
                else:
                    a["zan_status"] = "false"
                result["all_blog"].append(a)
            result["blogs"] = result["all_blog"]
        elif blog_type_id == -1:
            tuijian_blogs = CsdnBlog.objects.raw(
                """select * from csdnblog LEFT JOIN blogtype on csdnblog.blog_id=blogtype.id ORDER BY csdnblog.zan DESC ; """)[
                            (page - 1) * pagesize: page * pagesize]
            for tuijian_blog in tuijian_blogs:
                a = {}
                a["user_name"] = tuijian_blog.user_name
                a["id"] = tuijian_blog.id
                a["blog_intro"] = tuijian_blog.blog_intro
                # a["blog_content"] = all_csdnblog.blog_content
                a["blog_type"] = tuijian_blog.blog_type
                a["zan"] = tuijian_blog.zan
                a["liulan"] = tuijian_blog.liulan
                a["blog_time"] = tuijian_blog.blog_time
                a["blog_title"] = tuijian_blog.blog_title
                zancsdnblogs = ZanCsdnBlog.objects.filter(Q(blog_id=tuijian_blog.id) & Q(user_name=user_name)).order_by(
                    "-id")
                if zancsdnblogs:
                    zancsdnblog = zancsdnblogs[0]
                    is_true = zancsdnblog.zan_status
                    if is_true:
                        a["zan_status"] = "true"
                    else:
                        a["zan_status"] = "false"
                else:
                    a["zan_status"] = "false"
                result["tuijian_blog"].append(a)
            result["blogs"] = result["tuijian_blog"]
        else:
            blog_types = BlogType.objects.filter(id=blog_type_id)
            # if blog_types:
            #     blog_type = blog_types[0]
            # blog_types = BlogType.objects.all()
            # result["code"] = "001"
            # result["message"] = "查询成功"
            # result["all_blog"] = []
            # result["tuijian_blog"] = []
            # result["type_blogs"] = []
            # for all_csdnblog in all_csdnblogs:
            #     a = {}
            #     a["user_name"] = all_csdnblog.user_name
            #     a["id"] = all_csdnblog.id
            #     a["blog_intro"] = all_csdnblog.blog_intro
            #     # a["blog_content"] = all_csdnblog.blog_content
            #     a["blog_type"] = all_csdnblog.blog_type
            #     a["zan"] = all_csdnblog.zan
            #     a["liulan"] = all_csdnblog.liulan
            #     a["blog_time"] = all_csdnblog.blog_time
            #     a["blog_title"] = all_csdnblog.blog_title
            #     result["all_blog"].append(a)
            # for tuijian_blog in tuijian_blogs:
            #     a = {}
            #     a["user_name"] = tuijian_blog.user_name
            #     a["id"] = tuijian_blog.id
            #     a["blog_intro"] = tuijian_blog.blog_intro
            #     # a["blog_content"] = all_csdnblog.blog_content
            #     a["blog_type"] = tuijian_blog.blog_type
            #     a["zan"] = tuijian_blog.zan
            #     a["liulan"] = tuijian_blog.liulan
            #     a["blog_time"] = tuijian_blog.blog_time
            #     a["blog_title"] = tuijian_blog.blog_title
            #     result["tuijian_blog"].append(a)

            # for blog_type in blog_types:
            #     a = {}
            #     blog_type_id = blog_type.id
            #     blog_type_name = blog_type.blog_type
            #     print(blog_type_id)
            #     a[blog_type_name] = []
            if blog_types:
                # a = {}
                blog_type = blog_types[0]
                blog_type_name = blog_type.blog_type
                blogs = CsdnBlog.objects.filter(blog=blog_type).order_by("-blog_time")[
                        (page - 1) * pagesize: page * pagesize]
                # a[blog_type_name] = []
                # blogs = CsdnBlog.objects.raw(f"""select * from csdnblog where blog_id={blog_type_id} ORDER BY blog_time DESC""")
                for blog in blogs:
                    b = {}
                    b["user_name"] = blog.user_name
                    b["id"] = blog.id
                    b["blog_intro"] = blog.blog_intro
                    # a["blog_content"] = all_csdnblog.blog_content
                    b["blog_type"] = blog_type_name
                    b["zan"] = blog.zan
                    b["liulan"] = blog.liulan
                    b["blog_time"] = blog.blog_time
                    b["blog_title"] = blog.blog_title
                    zancsdnblogs = ZanCsdnBlog.objects.filter(
                        Q(blog_id=blog.id) & Q(user_name=user_name)).order_by(
                        "-id")
                    if zancsdnblogs:
                        zancsdnblog = zancsdnblogs[0]
                        is_true = zancsdnblog.zan_status
                        if is_true:
                            b["zan_status"] = "true"
                        else:
                            b["zan_status"] = "false"
                    else:
                        b["zan_status"] = "false"
                    # a[blog_type_name].append(b)
                    result["type_blogs"].append(b)
                result["blogs"] = result["type_blogs"]

        return JsonResponse(result)


# 根据关键字搜索获取博客数据
class SearchBlogView(APIView):
    def get(self, request, *args, **kwargs):
        result = {}
        user_name = request.GET.get("user_name", "")
        gjz = request.GET.get("gjz")
        page = request.GET.get("page", 1)
        pagesize = request.GET.get("pagesize", 15)
        page = int(page)
        pagesize = int(pagesize)
        print(gjz, page, pagesize)
        if gjz:
            blogs = CsdnBlog.objects.filter(blog_title__contains=gjz).order_by("-blog_time")[
                    (page - 1) * pagesize: page * pagesize]
            result["code"] = "001"
            result["datas"] = []
            if blogs:
                result["message"] = "查询成功"
                for blog in blogs:
                    a = {}
                    a["user_name"] = blog.user_name
                    a["id"] = blog.id
                    a["blog_intro"] = blog.blog_intro
                    # a["blog_content"] = blog.blog_content
                    # blogtypes = BlogType.objects.filter(id=blog.blog.id)
                    # if blogtypes:
                    #     blogtype = blogtypes[0]
                    #     blogtypename = blogtype.blog_type
                    # else:
                    #     blogtypename = ""
                    a["blog_type"] = blog.blog.blog_type
                    a["zan"] = blog.zan
                    a["liulan"] = blog.liulan
                    a["blog_time"] = blog.blog_time
                    a["blog_title"] = blog.blog_title
                    # a["blog_title"] = blog.blog_title.replace(gjz, f"""<view  style="color:red">{gjz}</view>""")
                    zancsdnblogs = ZanCsdnBlog.objects.filter(Q(blog_id=blog.id) & Q(user_name=user_name)).order_by(
                        "-id")
                    if zancsdnblogs:
                        zancsdnblog = zancsdnblogs[0]
                        is_true = zancsdnblog.zan_status
                        if is_true:
                            a["zan_status"] = "true"
                        else:
                            a["zan_status"] = "false"
                    else:
                        a["zan_status"] = "false"
                    result["datas"].append(a)

            else:
                result["message"] = "无查询结果"

        else:
            result["code"] = "002"
            result["message"] = "关键字为空，没有查询"
        print(result)
        return JsonResponse(result)


# 查看每个用户的最近浏览博客
class UserLLBlogView(APIView):
    def get(self, request, *args, **kwargs):
        result = {}
        user_name = request.GET.get("user_name", "1  2  3")
        page = request.GET.get("page", 1)
        pagesize = request.GET.get("pagesize", 15)
        page = int(page)
        pagesize = int(pagesize)
        print(user_name)
        llblogs = LiuLanCsdnBlog.objects.raw(
            f"""select *, max(liulan_time) as time from liulancsdnblog where user_name = '{user_name}' GROUP BY blog_id ORDER BY time DESC;""")[
                  (page - 1) * pagesize: page * pagesize]
        if llblogs:
            result["code"] = "001"
            result["message"] = "查询成功"
            result["datas"] = []
            for llblog in llblogs:
                a = {}
                # a["user_img"] = csdnblog.user_img
                a["user_name"] = llblog.blog.user_name
                a["id"] = llblog.blog.id
                a["blog_intro"] = llblog.blog.blog_intro
                # a["blog_content"] = llblog.blog.blog_content
                blogtypes = BlogType.objects.filter(id=llblog.blog.blog.id)
                if blogtypes:
                    blogtype = blogtypes[0]
                    blogtypename = blogtype.blog_type
                else:
                    blogtypename = ""
                a["blog_type"] = blogtypename
                a["zan"] = llblog.blog.zan
                a["liulan"] = llblog.blog.liulan
                t = str(llblog.time).split(".")[0]
                timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
                # 转换为时间戳:
                timeStamp = int(time.mktime(timeStruct))
                a["blog_time"] = time_(time.time() - timeStamp)
                # a["blog_time"] = llblog.blog.blog_time
                a["blog_title"] = llblog.blog.blog_title
                zancsdnblogs = ZanCsdnBlog.objects.filter(Q(blog_id=llblog.blog.id) & Q(user_name=user_name)).order_by(
                    "-id")
                if zancsdnblogs:
                    zancsdnblog = zancsdnblogs[0]
                    is_true = zancsdnblog.zan_status
                    if is_true:
                        a["zan_status"] = "true"
                    else:
                        a["zan_status"] = "false"
                else:
                    a["zan_status"] = "false"
                result["datas"].append(a)
        else:
            result["code"] = "002"
            result["message"] = "暂无数据"
            result["datas"] = []
        return JsonResponse(result)


class MySeachView(SearchView):
    # @property
    def create_response(self):  # 重载create_response来实现接口编写
        # result = {}
        # super(MySeachView, self).create_response()
        context = super(MySeachView, self).get_context()  # 搜索引擎完成后的内容
        print(context)
        keyword = self.request.GET.get('q', None)  # 关键子为q
        page = self.request.GET.get("page", 1)
        if not keyword:
            result = {}
            result["code"] = "002"
            result["message"] = "关键字为空，没有查询"
            return JsonResponse({"code": "002", "message": "关键字为空，没有查询"})
        content = {"status": {"code": 200, "msg": "ok"}, "datas": {
            "page": page, "next_page": page, "sort": '默认排序', }}
        content_list = []
        for i in context['page'].object_list:  # 对象列表
            a = {}
            a["user_name"] = i.object.user_name
            a["id"] = i.object.id
            blog_intro = i.object.blog_intro
            blog_intro = my_highlight(blog_intro, keyword)
            a["blog_intro"] = blog_intro
            # a["blog_content"] = blog.blog_content
            # blogtypes = BlogType.objects.filter(id=blog.blog.id)
            # if blogtypes:
            #     blogtype = blogtypes[0]
            #     blogtypename = blogtype.blog_type
            # else:
            #     blogtypename = ""
            a["blog_type"] = i.object.blog.blog_type
            a["zan"] = i.object.zan
            a["liulan"] = i.object.liulan
            a["blog_time"] = i.object.blog_time
            blog_title = i.object.blog_title
            blog_title = my_highlight(blog_title, keyword)
            a["blog_title"] = blog_title

            # set_dict = {
            #     'id': i.object.id, 'name': i.object.name, 'description': i.object.description,
            #     'brand': i.object.commodity.brand, 'describe': i.object.describe,
            #     'integral': i.object.integral, 'mall_price': i.object.mall_price,
            #     'market_price': i.object.market_price, 'inventory': i.object.inventory,
            #     'sales_volume': i.object.sales_volume,
            # }#要返回的字段
            # if i.object.specificationimage_set.filter(is_show=0):
            #     set_dict['show_image'] = i.object.specificationimage_set.filter(is_show=0)[0].image.url
            # else:
            #     set_dict['show_image'] = None
            content_list.append(a)
        content["datas"].update(dict(blogs=content_list))
        return JsonResponse(content)  # 对对象进行序列化返回json格式数据
