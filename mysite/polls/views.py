from django.http import HttpResponse

def index(request):
    return HttpResponse("メッセージを入力してください")