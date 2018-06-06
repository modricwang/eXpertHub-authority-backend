from django.http import HttpResponse
from authority_backend import models
import json
from definitions import *

from django.http.request import QueryDict
import os


def request_body_serialze(request):
    querydict = QueryDict(request.body.decode("utf-8"), encoding="utf-8")
    response_dict = {}
    try:
        for key, val in querydict.items():
            response_dict[key] = val
    except:
        pass
    return response_dict


root = 'authority_backend'
prefix = 'static'


def handle(request):
    if request.method == 'POST':
        print(request)
        errcode = RESPONSE_OK
        file = request.FILES.get('file')
        f = open(os.path.join(root, prefix, file.name), 'wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        s = {"errcode": errcode, 'path': os.path.join(prefix, file.name)}
    elif request.method == 'GET':
        errcode = 1
        s = {"errcode": errcode}
    else:
        errcode = 1
        s = {"errcode": errcode}
    s = json.dumps(s)
    return HttpResponse(s)
