from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.shortcuts import render_to_response
import stores.getDB


class Home(TemplateView):
    template_name = 'main.html'


def home(request):
    context = print_db()

    return render_to_response('main.html', context)


def print_db():
    context = stores.getDB.store
    context = {'stores': context, 'table_num': stores.getDB.table_num, 'table_status': stores.getDB.table_status}

    return context
