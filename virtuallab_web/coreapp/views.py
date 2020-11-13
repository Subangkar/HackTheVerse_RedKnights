from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Renders Home Page
    """
    template_name = 'coreapp/avilon/student-home.html'

    def get_context_data(self, **kwargs):
        ctx = {'loggedIn': self.request.user.is_authenticated}
        return ctx
