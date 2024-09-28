from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    message = ""
    form = UserCreationForm()
    #print(User.objects.filter(username="Xiujie"))  #get/all/filter 取得1筆/取得全部  若沒有名稱會出現DoesNotExist at /
    print(User.objects.all())
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        #print(request.POST.get("username"))   #容器

        # 密碼長度
        if len(password1) <8 or len(password2)!=8:
            message = "密碼長度不正確"
        elif password1!=password2:
            message = "兩次密碼不一樣"
        # 密碼相同(已測試)
        
        else:
            # 比對使用者是否存在
            if User.objects.filter(username=username):
                message="帳號已存在"
            #註冊使用者
            else:
                user=User.objects.create_user(username=username, password=password1)
                user.save()
                message="註冊成功!"
        

    return render(request,"user/register.html", {"form": form, "message":message}) #渲染到前端