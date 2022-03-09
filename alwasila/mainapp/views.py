from django.shortcuts import render


def plug(request):
    template = 'mainapp/plug.html'
    return render(request, template)


def index(request):
    template = 'mainapp/index.html'
    return render(request, template)
