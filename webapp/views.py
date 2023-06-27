from django.shortcuts import render


def to_do_list(request):
    return render(request, "list.html")
