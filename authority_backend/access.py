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
        if 'uid' in request.POST and 'rid' in request.POST:
            uid = int(request.POST['uid'])
            rid = int(request.POST['rid'])
            models.access.objects.create(uid=uid, rid=rid)
            s = 'ok'
        else:
            s = 'mmp'
    elif request.method == 'GET':
        errcode = 0
        l = None
        if 'uid' in request.GET:
            uid = int(request.GET['uid'])
            l = models.access.objects.filter(uid=uid)
        elif 'rid' in request.GET:
            rid = int(request.GET['rid'])
            l = models.access.objects.filter(rid=rid)
        else:
            l = models.access.objects.all()
        s = {"errcode": errcode, "list": []}
        if l is not None:
            for item in l:
                s["list"].append({'uid': item.uid, 'rid': item.rid})
        s = json.dumps(s)
    elif request.method == 'DELETE':
        body_dict = request_body_serialze(request)
        # print(request.body)
        # print(body_dict)
        uid = int(body_dict['uid'])
        rid = int(body_dict['rid'])
        models.access.objects.filter(uid=uid, rid=rid).delete()
        s = 'ok'
    else:
        s = 'unknown operation'
    return HttpResponse(s)
