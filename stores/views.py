from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
import stores.getDB
import stores.updateDB
import json


class Home(TemplateView):
    template_name = 'main.html'


def home(request):

    return render_to_response('main.html')


def autocomplete(request):
    # search_qs = ModelName.objects.filter(name__startswith=request.REQUEST['search'])

    store_names = stores.getDB.get_store_names()
    search_word = request.GET['search']

    results = {}

    for store_name in store_names:
        if search_word in store_name:
            results[store_name] = store_name

    return HttpResponse(json.dumps(results), content_type="application/json")


def store_status(request):
    context = print_db()

    if request.is_ajax():
        return HttpResponse(json.dumps({'store_name': context['store_name'], 'table_num': context['table_num'],
                                        'table_status': context['table_status']}), content_type="application/json")
    else:
        return render_to_response('store_status.html', context)


def print_db():
    context = stores.getDB.get_table_status('soongsil')
    table_status = context['table_status']
    # print(table_status)

    return context


def update_db(request):
    store_name = request.GET['storeName']
    table_number = "table_"+request.GET['tableNum']
    set_status = request.GET['setStatus']
    stores.updateDB.set_table_status(store_name, table_number, set_status)

    # print(request)

    home(request)

    context = print_db()

    return HttpResponse(json.dumps({'store_name': context['store_name'], 'table_num': context['table_num'],
                                    'table_status': context['table_status']}), content_type="application/json")


