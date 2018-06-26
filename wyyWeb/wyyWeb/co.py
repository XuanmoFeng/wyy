import json

import jieba.analyse
import matplotlib.pyplot as plt
import numpy as np
import pymysql
from PIL import Image
from django.http import HttpResponse
from wordcloud import WordCloud
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname("__file__")))

image = Image.open('timg.jpg')
graph = np.array(image)
wc = WordCloud(font_path='simhei.ttf', background_color='White', max_font_size=170, mask=graph)

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


def level(request):
    songId = request.GET.get('songId')
    # repetition = cursor.rowcount()
    # if repetition:
    #     pass
    # "SELECT count(sex) FROM wyy.user,wyy.song_coment where wyy.song_coment.songId=508297601 and wyy.song_coment.userId=wyy.user.userId and sex=1;"
    list2 = []
    for i in range(0, 10):
        cursor.execute(
            """select count(wyy.user.level) from wyy.user,wyy.song_coment where wyy.song_coment.songId=%s and wyy.song_coment.userId=wyy.user.userId and wyy.user.level=%s""",
            (557581284, i))
        num = cursor.fetchone()[0]
        d = {"department": "level%s" % i, "num": num}
        list2.append(d)
    resp = {"list": list2}
    # resp
    # resp = {"list":[{'department':"women ", 'num': 100}]}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def sex(request):
    resp = {"list": [{'num': 100}, {'num': 200}]}
    return HttpResponse(json.dumps(resp), content_type="application/json")


# #词频分析
def wn(request):
    print(BASE_DIR)
    l = ''

    cursor.execute(
        """SELECT content FROM wyy.comment,wyy.song_coment where wyy.comment.commentId=wyy.song_coment.commentId and wyy.song_coment.songId=508297601""")
    num = cursor.fetchall()
    for i in num:
        l += i[0]
    result = jieba.analyse.textrank(l, topK=250, withWeight=True)
    keyworlds = dict()
    for i in result:
        keyworlds[i[0]] = i[1]
    wc.generate_from_frequencies(keyworlds)


    # plt.imshow(wc)
    # # print(os.path)
    # # PIC_DIR=os.path.join(BASE_DIR, "..\\static\\images\\2.png")
    wc.to_file(BASE_DIR+'\\static\\images\\2.png')
    wc.to_image()
    return HttpResponse("<p>成功</p>")
