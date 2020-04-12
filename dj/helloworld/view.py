from django.http import HttpResponse
import json


# post
def hello(request):

    json_str = json.loads(request.body.decode())
    print(json_str)
    print(json_str['c'])
    return HttpResponse("hello world")


# get form
def hi(request):

    print(request.GET.get('a'))
    form_data = request.POST.get('c')
    print(form_data)
    return HttpResponse("hi")
