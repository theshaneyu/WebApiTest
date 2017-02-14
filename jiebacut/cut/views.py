from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import jieba


def cut(request):
    if request.POST and request.mothod == 'POST': # 如果確定有POST請求而且請求方法確實是POST
        data = request.POST
        data_dict = data.dict()
        return JsonResponse(jieba.lcut(data_dict['sentence']), safe=False)
    return HttpResponse('<h1>No POST request received!</h1>')
