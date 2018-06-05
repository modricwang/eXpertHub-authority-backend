from django.http import HttpResponse
from authority_backend import models
import json


def handle(request):
    if request.method == 'POST':
        if 'uid' in request.POST and 'rid' in request.POST:
            uid = int(request.POST['uid'])
            rid = int(request.POST['rid'])
            models.shoppingcart.objects.create(uid=uid, rid=rid)
    elif request.method == 'GET':
        errcode = 0
        l = None
        if 'uid' in request.GET:
            uid = int(request.GET['uid'])
            l = models.shoppingcart.objects.filter(uid=uid)
        elif 'rid' in request.GET:
            rid = int(request.GET['rid'])
            l = models.shoppingcart.objects.filter(rid=rid)
        else:
            l = models.shoppingcart.objects.all()
        s = {"errcode": errcode, "list": []}
        if l is not None:
            for item in l:
                s["list"].append({'uid': item.uid, 'rid': item.rid})
        s = json.dumps(s)
    else:
        s = 'unknown operation'
    return HttpResponse(s)
