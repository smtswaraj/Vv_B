from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def about(request):
    
    return render(request,'about.html')    

def contact(request):
    
    return render(request,'contact.html')

def appads(request):
    

    f = open('static/app-ads.txt', 'r')
    file_content = f.read()
    f.close()

    return HttpResponse(file_content, content_type="text/plain")    