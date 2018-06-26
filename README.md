# 网易云音乐爬虫分为了四个模块
## 1.对歌手的信息进行爬取，分别爬取歌手的id和名字，以及他所在的分类。代码在Singer.py中
## 2.对歌手的专辑信息进行爬取，爬取专辑的每个歌手的专辑信息，在albumSpider里
## 3.将专辑中的歌曲信息进行爬取，爬取下来的歌曲和歌曲名字，歌曲id，歌曲的时间长度
## 4.对歌曲中的评论进行爬取
## 5.对评论者的信息进行爬取

每个模块相互独立。更好的管理
## 所采用的技术：
scrapy-redis：分布式爬虫框架
echarts：统计图的分析
Django：前端的显示
一些反爬虫工具