# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.GET.get('text','default')
    
    removepunc = request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase','off')
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in djtext:
            if ele in punctuations:
                djtext = djtext.replace(ele, "")
    if uppercase=="on":
        lis=list(djtext)
        for i in range(len(lis)):
            lis[i]=lis[i].upper()
        djtext="".join(lis)

    params={'analyzed_text':djtext}
    return render(request,'analyze.html',params)


