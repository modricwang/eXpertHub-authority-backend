from django.http import HttpResponse
from authority_backend import models
import json

from django.http.request import QueryDict


def request_body_serialze(request):
    querydict = QueryDict(request.body.decode("utf-8"), encoding="utf-8")
    response_dict = {}
    try:
        for key, val in querydict.items():
            response_dict[key] = val
    except:
        pass
    return response_dict


def handle(request):
    if request.method == 'POST':
        file = request.FILES["file"]
        models.storage.objects.create(file=file)
        s = 'OK'
    elif request.method == 'GET':
        s = 'OK'
    else:
        s = 'mmp'
    return s
