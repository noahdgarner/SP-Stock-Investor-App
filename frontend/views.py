from django.shortcuts import render
import os, random, string
from Screener.User import User
from Screener.Analyzer import Analyzer
from Screener.report_generator import reportGenerator
from ratelimit.decorators import ratelimit
from django.template.loader import render_to_string
# from django.http import HttpResponse
# Create your views here.


def home(request):

    context = {}

    return render(request, "frontend/index.html", context)

def select(request):


    if request.method == "POST":
        full_str = request.body.decode("utf-8")
        print(full_str)
        full_str = full_str.split("&fname=")[1]
        fname = full_str.split("&lname=")[0]
        full_str = full_str.split("&lname=")[1]
        lname = full_str.split("&email=")[0]
        full_str = full_str.split("&email=")[1]
        email = full_str.split("&level=")[0]
        full_str = full_str.split("&level=")[1]
        level = int(full_str.split("&risk=")[0])
        full_str = full_str.split("&risk=")[1]
        risk = int(full_str.split("&signup=")[0])


    name = fname + "+" + lname

    returnstring = name+"/"+email+'/'+str(risk)+'/'+str(level)

    print(returnstring)

    context = {'userinfo': returnstring}

    return render(request, "frontend/sectorselect.html", context)


@ratelimit(key='ip', rate='500/s')
def app(request):

    if request.method == "POST":
        full_str = request.body.decode("utf-8")
        full_str = full_str.split("&userinfo=")[1]
        full_str = full_str.split('&signup=')[0]
        full_str = full_str.replace("%2F", '/')
        full_str = full_str.replace("%2540", '@')
        full_str = full_str.replace("%2B", '+')
        print(full_str)
        name, email, risk, level = full_str.split('/')
        fname, lname = name.split("+")

        fullname = fname + " " + lname

        risk = int(risk)
        level = int(level)

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

    analyzer = Analyzer(user.user_to_json())

    analyzer.analysis()
    profile = analyzer.company_profile
    generate = reportGenerator(user, analyzer.finance_reasons, profile)
    generate.generate_report()

    # path = (analyzer.img_path).split("static/")[1]
    print(analyzer.img_path)
    stat_path = analyzer.img_path.split('static/')[1]

    context = {
        'name': user.firstName,
        'ticker': generate.ticker,
        'english': generate.written,
        'graphpath': stat_path
    }

    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    stat_path = 'frontend/static/output/' + code + '.html'

    save_path = os.path.abspath(os.path.join(stat_path))
    content = render_to_string('frontend/output.html', context)
    with open(save_path, 'w') as static_file:
        static_file.write(content)
    return render(request, "frontend/output.html", context)