from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.shortcuts import render_to_response


class Home(TemplateView):
    template_name = 'main.html'


def home(request):
    return render_to_response('main.html')
