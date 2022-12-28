from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = "home/home.html"
    extra_context = {"today": datetime.today()}


class AuthorizedView(
    LoginRequiredMixin,
    TemplateView,
):
    template_name = "home/authorized.html"
    login_url = "/admin"


# # Create your views here.
# def home(request):
#     return render(
#         request=request,
#         template_name="home/home.html",
#         context={"today": datetime.now()},
#     )
