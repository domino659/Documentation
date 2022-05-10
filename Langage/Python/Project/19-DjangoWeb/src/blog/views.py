from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Le Blog</h1>")
    return render(request, "Blog/index.html")

def article(request, numero_article):
    if numero_article in ["01", "O2", "03"]:
        return render(request, f"blog/article_{numero_article}.html")
    return render(request, "blog/article_not_found.html")