from django.http import HttpResponse
from authority_backend import models
import json
from definitions import *
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
            uid = str(request.POST['uid'])
            rid = str(request.POST['rid'])
            models.shoppingcart.objects.create(uid=uid, rid=rid)
            s = RESPONSE_OK
        else:
            s = RESPONSE_ERR
    elif request.method == 'GET':
        errcode = 0
        l = None
        if 'uid' in request.GET:
            uid = str(request.GET['uid'])
            l = models.shoppingcart.objects.filter(uid=uid)
        elif 'rid' in request.GET:
            rid = str(request.GET['rid'])
            l = models.shoppingcart.objects.filter(rid=rid)
        else:
            l = models.shoppingcart.objects.all()
        s = {"errcode": errcode, "list": []}
        if l is not None:
            for item in l:
                s["list"].append({'uid': item.uid, 'rid': item.rid})
        s = json.dumps(s)
    elif request.method == 'DELETE':
        body_dict = request_body_serialze(request)
        # print(request.body)
        # print(body_dict)
        uid = str(body_dict['uid'])
        rid = str(body_dict['rid'])
        models.shoppingcart.objects.filter(uid=uid, rid=rid).delete()
        s = RESPONSE_OK
    else:
        s = RESPONSE_ERR
    return HttpResponse(s)
