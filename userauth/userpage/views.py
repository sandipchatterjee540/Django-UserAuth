from django.shortcuts import render, HttpResponse, redirect
from userpage.models import Singin
from django.contrib import messages
from datetime import datetime


# Create your views here.
def singin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        date = datetime.now()
        if username and email and password and password1:
            if password == password1:
                db_user = Singin.objects.filter(username=username)
                db_email = Singin.objects.filter(email=email)
                if db_user:
                    messages.success(request, 'This name {} already exist'.format(username))
                    dic = {
                        "sta": "danger",
                    }
                    return render(request, "singin.html", dic)
                elif db_email:
                    messages.success(
                        request, 'This email {} already exist'.format(email))
                    dic = {
                        "sta": "danger",
                    }
                    return render(request, "singin.html", dic)
                else:
                    model = Singin(username=username, email=email,password=password, date=date)
                    model.save()
                    messages.success(request, 'HI {} Now we can join us'.format(username))
                    dic = {
                        "sta": "sucess",
                    }
                    return render(request, "login.html", dic)

            else:
                messages.warning(
                    request, 'Password not match please enter carefully')
                dic = {
                    "sta": "danger",
                }
                return render(request, "singin.html", dic)
        else:
            messages.warning(
                request, 'Please fill up this from carefully If you have already account click login')
            dic = {
                "sta": "danger",
            }
            return render(request, "singin.html", dic)
    else:
        return render(request, "singin.html")



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        db_user = Singin.objects.filter(username=username, password=password)
        if db_user:
            dic = {
                "name": db_user[0],
                "sta": "success",
            }
            messages.success(request, 'HI {} YOU ARE SUCESSFULLY LOGIN '.format(username.upper()))
            return render(request, "home.html", dic)
        else:
            messages.warning(request, 'This is not vaild user')
            dic = {
                "sta": "danger",
            }
            return render(request, "login.html", dic)

    return render(request, "login.html")


def home(request):
    # return redirect(request,"login.html")
    return render(request, "login.html")
