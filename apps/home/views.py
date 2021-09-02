from django.shortcuts import render


def HomeView(request):
    template_name = "home/home.html"

    context = {}

    # return render(request, template_name, context)
    return render(request, template_name)