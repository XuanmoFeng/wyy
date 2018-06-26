# AlubumSpider
## 专辑爬虫
#### 爬虫歌手的专辑信息
- 在redis里面插入专辑的url进行爬取，爬取的信息
- 比如爬取歌手id为12345de 信息
- 其中包括专辑的时间和专辑的名称，专辑的图片，专辑的id值

    lpush albumsipder:strat_urls http://music.163.com/artist/album?id=12345&limit=100

#### 启动的方式scrapy crawl album
#### 保存到数据库中
- setting文件中配置了数据库的配置
- 其中也配置了redis的地址
<meta http-equiv="refresh" content="0.5">