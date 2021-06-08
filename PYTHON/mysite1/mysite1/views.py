# yshen
# 2021/5/18 11:26
# from django.http import HttpResponse
#
# def page_2003_view(request):
#     html='<h1>这是第一个页面</h1>'
#     return HttpResponse(html)
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

def page_2003_view(request):
    html='<h1>这是第一个页面</h1>'
    return HttpResponse(html)

def index(request):
    if request.method=='GET':
        print(request.GET['a'])
        print(request.GET.get('c','no c'))
    return HttpResponse("Hello, world.This is index.")

def pagen_view(request,pg):
    html = '<h1>这是第%s个页面</h1>'%(pg)
    return HttpResponse(html)

def cal_view(request,n,op,m):
    if op not in ['add','sub','mul','dev']:
        return HttpResponse('op error')
    result = 0
    if op=='add':
        result = n + m
    elif op=='sub':
        result = n - m
    elif op=='mul':
        result = n * m
    elif op=='dev':
        result = n / m
    html = '<h1>计算结果为:%s</h1>'%result
    return HttpResponse(html)

def cal_view2(request,x,op,y):
    if op not in ['add','sub','mul','dev']:
        return HttpResponse('op error')
    result = 0
    x = int(x)
    y = int(y)
    if op=='add':
        result = x + y
    elif op=='sub':
        result = x - y
    elif op=='mul':
        result = x * y
    elif op=='dev':
        result = x / y
    html = '<h1>计算结果为:%s</h1>'%result
    return HttpResponse(html)

def birthday_view(request,y,m,d):
    html = '出日为:%s年%s月%s日' %(y,m,d)
    return HttpResponse(html)

def test_html(request):
    #方案1
    # t = loader.get_template('test_html.html');
    # html = t.render()
    # return HttpResponse(html)
    #方案2
    dict={
        'name':'zhangsan',
        'age':20
    }
    return render(request,'test_html.html',dict)

def test_if_for(request):
    dict={}
    dict['x'] = 9
    return render(request, 'test_if_for.html', dict)

def base_view(request):
    return render(request, 'base.html')

def music_view(request):
    return render(request, 'music.html')

def sport_view(request):
    return render(request, 'sport.html')

def test_url(request):
    return render(request, 'test_url.html')

def test_url_result(request):
    from django.urls import reverse
    url = reverse('base_index')
    return HttpResponseRedirect(url)
    # return HttpResponse('---test url res is ok')