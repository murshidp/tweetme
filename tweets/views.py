from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse 
from.models import Tweet
import random
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html")

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{"id":x.id,"content":x.content,"likes":random.randint(0, 120)} for x in qs]
    data = {
        "response":tweet_list,
        "isUser":False
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id":tweet_id,
        
    }
    status=200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
    except:
        data['message']="Not found"
        status=404
   
    return JsonResponse(data,status=status)



