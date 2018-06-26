from django.db import models


# 专辑实体
class AlbumItem(models.Model):
    albumid = models.IntegerField()
    singerid = models.IntegerField()
    albumname = models.CharField(max_length=255)
    albumpic = models.CharField(max_length=255)
    albumtime = models.CharField(max_length=255)

    class Meta:
        db_table = 'album'


# 歌手实体
class SingerItem(models.Model):
    singerId = models.IntegerField()
    zimu = models.IntegerField()
    fenlei = models.IntegerField()
    pic = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'singer'


# 评论实体
class CommentItem(models.Model):
    commentId = models.IntegerField()
    liked = models.IntegerField()
    likedCount = models.IntegerField()
    time = models.DateTimeField(max_length=255)
    content = models.CharField(max_length=1000)
    userId = models.IntegerField()
    beReplied = models.IntegerField()

    class Meta:
        db_table = 'comment'


# 用户实体
class UserItem(models.Model):
    userId_id = models.IntegerField()
    name = models.CharField(max_length=500)
    level = models.IntegerField()
    dt = models.DateField()
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    sex = models.IntegerField()
    event = models.IntegerField()
    follows = models.IntegerField()
    fans = models.IntegerField()
    described = models.CharField(max_length=500)
    weibo = models.CharField(max_length=255)
    douban = models.CharField(max_length=255)
    authStatus = models.IntegerField()
    avatarUrl = models.CharField(max_length=255)
    expertTags = models.CharField(max_length=45)
    experts = models.CharField(max_length=45)
    locationInfo = models.CharField(max_length=45)
    remarkName = models.CharField(max_length=45)
    userType = models.IntegerField()
    vipType = models.IntegerField()

    class Meta:
        db_table = 'user'


# 歌曲评论实体
class SongCommentItem(models.Model):
    class Meta:
        db_table = 'song_coment'
    userId=models.ForeignKey(to="UserItem",on_delete=models.CASCADE)
    songId = models.IntegerField()
    commentId = models.IntegerField()


# 歌曲实体
class SongItem(models.Model):
    songid = models.IntegerField()
    albumid = models.IntegerField()
    singerid = models.IntegerField()
    length = models.CharField(max_length=255)
    songname = models.CharField(max_length=255)

    class Meta:
        db_table = 'song'
