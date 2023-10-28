from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def name(request):
    return render(request, "meu_nome.html",{})