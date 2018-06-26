import pymysql
import redis
from album_list.models import AlbumItem, SingerItem, SongItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import QuerySet
from django.http import HttpResponse
from django.template.loader import get_template

# mysql数据库多表查询
connect = pymysql.connect(
    host='123.207.244.108',
    port=3306,
    db='wyy',
    user='root',
    passwd='123456',
    charset='utf8',
    use_unicode=True)

cursor = connect.cursor()
# 需求先启动redis服务器
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379)
CONN = redis.Redis(connection_pool=POOL)


#
def list_album(request):
    """显示歌手的专辑信息"""
    t = get_template("album.html")
    singerId = request.GET.get('singerId')
    test2 = SingerItem.objects.get(singerId=1883)
    singername = test2.name
    lists = AlbumItem.objects.filter(singerid=singerId)
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


def album_detail(request):
    """显示专辑中的歌曲信息"""
    albumId = request.GET.get('albumId')
    leixin = "专辑"
    lists = QuerySet()
    name = ""
    if albumId is None:
        lists = SongItem.objects.get_queryset().order_by('id')
    else:
        lists = SongItem.objects.filter(albumid=albumId)
        print(lists)
    if lists:
        t = get_template("albumDetail.html")
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
    else:
        t = get_template("spider.html")
        id = albumId
        name = AlbumItem.objects.get(albumid=albumId).albumname
        kind = "专辑"
        kindId = 1
        html = t.render(locals())
        return HttpResponse(html)


def spider(request):
    """启动爬虫的信息"""
    kind = request.GET.get('kindId')
    key = ""
    url = ""
    id = request.GET.get('id')
    if kind == '1':
        # 爬取专辑内的歌曲信息
        key = "songSpider:start_urls"
        url = "https://music.163.com/album?id=%s" % id
    elif kind == '2':
        # 爬取歌曲评论及评论者的信息
        key = "comment:start_url"
        url = "https://music.163.com/weapi/v1/resource/comments/R_AL_3_%s?csrf_token=" % id
    CONN.lpush(key, url)
    return HttpResponse("<p>开始爬取</p>")


def analysis(request):
    """分析函数"""
    t = get_template("commentator.html")
    songId = request.GET.get('songId')
    html = t.render(locals())
    return HttpResponse(html)
