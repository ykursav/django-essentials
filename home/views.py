from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(
        request=request,
        template_name="home/home.html",
        context={"today": datetime.now()},
    )


@login_required(login_url="/admin")
def authorized(request):
    return render(request=request, template_name="home/authorized.html", context={})
