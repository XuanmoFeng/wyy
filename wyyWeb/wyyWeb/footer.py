from django.http import HttpResponse


def footer():
    return HttpResponse("<p>信息是</p>")

