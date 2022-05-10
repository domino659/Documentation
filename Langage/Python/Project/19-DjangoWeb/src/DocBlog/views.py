from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render

def index(request):   
    # return HttpResponse("<h1>Bonjour, bienvenue sur mon site</h1>")
    return render(request, "DocBlog/index.html", context={"date": datetime.today()})