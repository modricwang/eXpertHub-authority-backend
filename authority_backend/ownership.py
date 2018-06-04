from django.http import HttpResponse


def handle(request):
    if request.method == 'POST':
        s = 'POST SUCCESS'
    elif request.method == 'GET':
        s = 'GET SUCCESS'
    else:
        s = 'unknown operation'
    return HttpResponse(s)
