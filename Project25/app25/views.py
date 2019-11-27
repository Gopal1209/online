from django.contrib import messages
from django.shortcuts import render,redirect
from .models import LoginDetails

def showIndex(request):
    try:
        value  = request.session["user"]
        return render(request,"welcome.html",{'data':value})
    except KeyError:
        return render(request,"index.html")


def logincheck(request):
    email = request.POST["email"]
    upass = request.POST["upass"]
    try:
        res = LoginDetails.objects.get(email=email,password=upass)
    except LoginDetails.DoesNotExist:
        #return render(request,"index.html",{"error":"Invalid User"})
        messages.error(request,"Sorry.. Invalid User")
        return redirect("main")
    else:
        # Writing uname to session
        request.session["user"] = email
        #request.session.set_expiry(0)
        request.session.set_expiry(60)

        return render(request,"welcome.html",{"data":email})


def logout(request):
    # deleting uname from session
    del request.session["user"]
    return render(request,"index.html")


def Register(request):
    return render(request, "register.html")


def Signup(request):
    username = request.POST["uname"]
    email = request.POST["email"]
    cont = request.POST["cont"]
    password = request.POST["upass"]
    LoginDetails(username=username, email=email, contact=cont, password=password).save()
    return redirect('main')