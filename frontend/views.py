from django.shortcuts import render
from Screener.User import User
#from django.http import HttpResponse
# Create your views here.


def home(request):

    context = {}

    return render(request, "frontend/index.html", context)


def app(request):

    if request.method == "POST":
        full_str = request.body.decode("utf-8")
        full_str = full_str.split("name=")[1]
        name = full_str.split("&email=")[0]
        full_str = full_str.split("&email=")[1]
        email = full_str.split("&level=")[0]
        full_str = full_str.split("&level=")[1]
        level = int(full_str.split("&risk=")[0])
        full_str = full_str.split("&risk=")[1]
        risk = int(full_str.split("&signup=")[0])


        fname, lname = name.split('+')

        fullname = fname + " " + lname

        email = email.replace('%40', '@')


    else:

        fname = "Jesse"
        lname = "Hill"
        fullname = fname + " " + lname
        email = "j_hill14@.pacific.edu"
        risk = 10
        level = 1

    print("\n****************************")
    print(fullname, email, risk, level)

    user = User(fname, lname, risk, level)

    user.generate_screen_url()
    user.run_all_empty_screen()

    context = {}

    return render(request, "frontend/output.html", context)