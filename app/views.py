from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def uday(resqest):
    return HttpResponse("Hello, world. You're at the uday page.")


def chandu(request):
    return HttpResponse("<h1>You're at the chandu page.</h1>")


def bharath(request):
    return HttpResponse("<h1><marquee>You're at the bharath page.</marquee></h1>")


def ub(request):
    return HttpResponse('''
    <h1 style="color:red"><marquee>HELLO WORLD!!!!</marquee></h1>
    <h1>my name is udaykiran</h1><br>
    <h2>my age is 22</h2><br>
    <h3>my place is tirupati</h3><br>
    <h4>my college is siddharth institute engineer and technology</h4><br>
    <h5 style="color:blue">my branch is MCA</h5><br>
    ''')