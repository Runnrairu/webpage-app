from django.http import HttpResponse
from .models import *
from django.utils import timezone

def index(request):
    res = HttpResponse(request.GET["url"])
    return res

def get_list(request):
    mes = Message.objects.all()
    res = ""
    
    for m in mes:
        res += "{0},{1},{2}<br>".format(m.date ,m.sender,m.text)
    return HttpResponse(res)

def add_message(request):
    q = Message(date=timezone.now (),sender=request.META.get('REMOTE_ADDR') , text = request.GET.get("text") )
    q.save ()
    return HttpResponse("入力成功")
    