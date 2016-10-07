from django.http import HttpResponse
from django.template import loader

def accesshomepage(request):
    template = loader.get_template('web/homepage.html')
    return HttpResponse(template.render(request))

def accessinfopage(request):
    template = loader.get_template('web/info.html')
    return HttpResponse(template.render(request))