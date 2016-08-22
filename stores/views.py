from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
import stores.getDB
import json


class Home(TemplateView):
    template_name = 'main.html'


def home(request):
    context = print_db()

    if request.is_ajax():
        return HttpResponse(json.dumps({'store_name': context['store_name'], 'table_num': context['table_num'],
                                        'table_status': context['table_status']}), content_type="application/json")
    else:
        return render_to_response('main.html', context)


def print_db():
    context = stores.getDB.get_table_status('soongsil')
    table_status = context['table_status']
    # print(table_status)

    return context
