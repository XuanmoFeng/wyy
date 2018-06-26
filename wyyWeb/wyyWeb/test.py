# from django.shortcuts import get_tempalte
import json

from album_list.models import SingerItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template.loader import get_template


def test(request):
    """显示歌手的信息"""
    response = ""
    response1 = ""
    t = get_template("test.html")
    lists = SingerItem.objects.get_queryset().order_by('id')
    paginator = Paginator(lists, 10)
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)
    it = range(1, 10)
    try:
        lists = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        lists = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        lists = paginator.page(paginator.num_pages)
    html = t.render(locals())
    return HttpResponse(html)


def index(request):
    """加载首页"""
    t = get_template("footer.html")
    return HttpResponse(t.render())


def search(request):
    """搜索处理"""
    param = request.GET.get('singerId')
    t = get_template("singer.html")
    return HttpResponse(t.render())


def commentator(request):
    """评论者用户"""
    t = get_template("commentator.html")
    return HttpResponse(t.render())


def comment(request):
    """评论"""
    t = get_template("comment.html")
    return HttpResponse(t.render())

