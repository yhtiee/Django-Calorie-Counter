from django.shortcuts import render

# Create your views here.
def Virtual_page(request):
    return render(request, "db/virtualpage.html")

def Landingpage(request):
    return render (request, "db/landingpage.html", {"active": "landingpage"})