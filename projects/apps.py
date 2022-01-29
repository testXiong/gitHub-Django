import json

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from  django.views import View
from django.apps import AppConfig



# 方法视图，根据请求的类型返回不同的方法，
def index(request):
    if  request.method== "GET":
        return HttpResponse("<h1>这是一个get方法</h1>")
    elif request.method=="POST":
        return HttpResponse("<h1>这是一个post方法</h1>")
    elif request.method=="DELETE":
        return HttpResponse("<h1>这是一个delete方法</h1>")
    elif request.method=="PUT":
        return HttpResponse("<h1>这是一个put方法</h1>")
    else:
        return HttpResponse("<h1>没有找到任何方法</h1>")

#类视图，根据请求的类型，调用不同的类， 注 post\get\put这些只能用小写与请求方法一一对应
class IndexView(View):
    def get(self,request):
        return HttpResponse("<h1>这是一个get1方法</h1>")
    def post(self,request):
        return HttpResponse("<h1>这是一个post1方法</h1>")
    def delete(self,request):
        return HttpResponse("<h1>这是一个delete1方法</h1>")
    def put(self,request):
        return HttpResponse("<h1>这是一个put1方法</h1>")

#  请求时调用html
class IndexRender(View):
    def get(self,request): # get 方法为前后端不分离方法

        data = [
            {
                "project_name": "探索火星项目",
                "leader": "一夜崔人泪",
                "app_name": "探索火星应用"
            },
            {
                "project_name": "小熊XXX应用项目",
                "leader": "Android程序",
                "app_name": "XXX应用"
            },
            {
                "project_name": "小张XXX应用项目",
                "leader": "IOS小程序",
                "app_name": "XXX应用"
            }]
# request 为第一个参数，请求类型
#"demo.html" 请求模版
# locals() 为请求方法，把本地列表上传
        return render(request,"demo.html",locals())
    def post(self,request): #post 为前后端分离方法
        data = [
            {
                "project_name": "探索火星项目",
                "leader": "一夜崔人泪",
                "app_name": "探索火星应用"
            },
            {
                "project_name": "小熊XXX应用项目",
                "leader": "Android程序",
                "app_name": "XXX应用"
            },
            {
                "project_name": "小张XXX应用项目",
                "leader": "IOS小程序",
                "app_name": "XXX应用"
            }]
        return JsonResponse(data,safe=False)
    def delete(self,request):
        return HttpResponse("<h1>这是一个delete1方法</h1>")
    def put(self,request):
        return HttpResponse("<h1>这是一个put1方法</h1>")

class IndexJsonResponse(View):

    def get(self,request):
        '''
        1.request 是HttpRequest对象，相当于请求报文
        2.可以使用request.GET 获取查询字符中参数
        3. 获取的是QueryDict对象，可以类比于字典，可以使用[]或者.get（）方法去获取具体的值
        4.如果有多个相同的key ,可以使用getlist（key）方法获取

        '''
        data = [
            {
                "project_name": "探索火星项目",
                "leader": "一夜崔人泪",
                "app_name": "探索火星应用"
            },
            {
                "project_name": "小熊XXX应用项目",
                "leader": "Android程序",
                "app_name": "XXX应用"
            },
            {
                "project_name": "小张XXX应用项目",
                 "leader": "IOS小程序",
                "app_name": "XXX应用"
            }]
        return JsonResponse(data,safe = False)

    def post(self,request):
        # 如果要获取 json的数据，需要从请求体中获取
        #1. 可以使用request.post来获取 www-from表单类型的参数
        #2.获取的是QueryDict对象，可以类比于字典，可以使[]或者.get()方法去获取具体的值
        #3.如果有多个相同的key.可以使用getlist(Key)方法获取

        return HttpResponse("这是一个前后端分离的post")

    def put(self,request,pk):
        #1.接收json 参数的转换
        # jsonl转换方法1： eval(request.body.decode('utf-8') )查询返回的json ,eval是解析的意思  注：eval不能解析 True Flase
        # jsonl转换方法2： json.dumps() -json, json.loads()->json 字典
        #2. request.Files 传文件
        #3. 路径参数转换器（int 、slug 、uuid等）
        # 接收路径ID <int:pk>，pk是给路径参数命名
        #4.如果以请求头类型传参
        #可以使用request.META来获取
        #HTTP_作为前缀，_请求头参数key(大写)，例如：request.META['HTTP_AGE']
        #注： Content-Type ，token 等内置请求头可以忽略

        print( json.loads(request.body.decode('utf-8')))  #打印出请求传参

        return HttpResponse('这是一个前后端分离的put')



class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'


