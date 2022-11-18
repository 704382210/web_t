from django.shortcuts import render,render_to_response
from  allModel import userModel
# 访问首页
def index(request):
    return render_to_response("user/index.html")

# 注册
def register(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        usercode = request.POST.get("usercode",None)
        twz = userModel.user.objects.create(username=username, password=password, usercode=usercode)
        twz.save()
    return render(request,"user/register.html")

# 展示用户信息
def userList(request):
    user_list = userModel.user.objects.all()
    return render(request,"user/showUser.html",{"userList":user_list})