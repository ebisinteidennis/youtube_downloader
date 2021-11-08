from django.shortcuts import render
#Pytube pakage for downloading youtube videos
from pytube import YouTube


def ytb_down(request):
    return render(request,'base/main.html')

def ytb_downloader(request):
    url = request.GET.get('url')
    obj = YouTube(url)
    resolutions = []
    strm_all = obj.stream.all()
    for i in strm_all:
        resolutions.append(i.resolutions)
    print(resolutions)

    return render(request,'base/download.html')