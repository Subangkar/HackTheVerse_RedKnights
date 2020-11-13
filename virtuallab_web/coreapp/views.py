from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

USERID_MAP_FOR_DEMO = {
    'subangkar': 'Student',
    'araf': 'Student',
    'samin': 'Student',
    'joseph': 'Teacher',
    'andrew': 'Teacher',
}


class Index(TemplateView):
    """
    Renders Home Page
    """
    template_name = 'coreapp/avilon/student-home.html'

    def get_context_data(self, **kwargs):
        ctx = {'loggedIn': self.request.user.is_authenticated}
        return ctx


class Login(TemplateView):
    """
    Renders Home Page
    """

    template_name = 'coreapp/avilon/login.html'

    def get_context_data(self, **kwargs):
        ctx = {'loggedIn': self.request.user.is_authenticated}
        return ctx

    def post(self, request, *args, **kwargs):
        try:
            name = str(request.POST.get('name')).strip().lower()
            if name in USERID_MAP_FOR_DEMO:
                login(request, user=User.objects.get(username=name))
                return redirect('/')
        except:
            pass
        return HttpResponse("Invalid data")


def logout_user(request):
    logout(request)
    return redirect('/')
