from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import jieba


def cut(request):
    text = ['沒有收到POST請求']
    if request.POST and request.method == 'POST': # 如果確定有POST請求而且請求方法確實是POST
        data = request.POST
        data_dict = data.dict()
        print("123")
        return JsonResponse(jieba.lcut(data_dict['sen']), safe=False)
    print("456")
    return JsonResponse(text)
