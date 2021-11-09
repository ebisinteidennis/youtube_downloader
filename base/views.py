from django.shortcuts import render
from django.urls import resolvers
#Pytube pakage for downloading youtube videos
from pytube import YouTube


def ytb_down(request):
    return render(request,'base/main.html')

def ytb_downloader(request):
    url = request.GET.get('url')
    obj = YouTube(url)
    resolutions = []
    strm_all = obj.streams.all()
    for i in strm_all:
        resolutions.append(i.resolution)
    resolutions = list(dict.fromkeys(resolutions))
    print('resolutions: ',resolutions)

    return render(request,'base/download.html',{'rls': resolutions})