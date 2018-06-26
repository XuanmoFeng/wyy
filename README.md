# 网易云音乐爬虫分为了四个模块
- 1.对歌手的信息进行爬取，分别爬取歌手的id和名字，以及他所在的分类。代码在Singer.py中
- 2.对歌手的专辑信息进行爬取，爬取专辑的每个歌手的专辑信息，在albumSpider里
- 3.将专辑中的歌曲信息进行爬取，爬取下来的歌曲和歌曲名字，歌曲id，歌曲的时间长度
- 4.对歌曲中的评论进行爬取
- 5.对评论者的信息进行爬取

### 每个模块相互独立。更好的管理
- 前端结构如下：
![前端结构图](https://github.com/XuanmoFeng/wyy/blob/master/image/jiegou.png)
- 后端结构如下：
![后端结构图](https://github.com/XuanmoFeng/wyy/blob/master/image/houduan.png)
- # 原理图
![原理](https://github.com/XuanmoFeng/wyy/blob/master/image/yuanli.png)
## 所采用的技术：
scrapy-redis：分布式爬虫框架
echarts：统计图的分析
Django：前端的显示
一些反爬虫工具
## 页面的显示
![男女比例分析](https://github.com/XuanmoFeng/wyy/blob/master/image/sex.jpg)
![地图区域分析](https://github.com/XuanmoFeng/wyy/blob/master/image/map.jpg)
![等级分布分析](https://github.com/XuanmoFeng/wyy/blob/master/image/level.jpg)
![专辑列表](https://github.com/XuanmoFeng/wyy/blob/master/image/albumlist.jpg)
