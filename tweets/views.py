from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse 
from.models import Tweet
# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("hello world") 

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    
    return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}")



