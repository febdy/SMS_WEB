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
    context = get_store_info_db()
    context = {'context': context}

    return render_to_response('main.html', context)


def autocomplete(request):
    store_names = get_store_names_db()
    search_word = request.GET['search_word']

    results = {}

    for store_name in store_names:
        if search_word in store_name:
            results[store_name] = store_name

    return HttpResponse(json.dumps(results), content_type="application/json")


def search(request):
    search_word = request.GET.get("searchBox")

    context = get_store_info_db()
    results = []

    for store in context:
        if search_word in store['store_name']:
            results.append(store)

    context = {'context': results}

    return render_to_response('main.html', context)


def store_status(request, store_name):
    context = get_table_status_db(store_name)
    context['range'] = range(1, context['table_num']+1)

    if request.is_ajax():
        return HttpResponse(json.dumps({'table_status': context['table_status'], 'if_modified': context['if_modified']})
                            , content_type="application/json")
    else:
        return render_to_response('store_status.html', context)


def update_db(request):
    store_name = request.GET['storeName']
    table_number = "table_"+request.GET['tableNum']
    set_status = request.GET['setStatus']
    modified_number = "modified_"+request.GET['tableNum']
    modified = request.GET['modified']
    update_table_status(store_name, table_number, set_status, modified_number, modified)


def get_store_info_db():
    context = stores.getDB.get_store_info()

    return context


def get_table_status_db(store_name):
    context = stores.getDB.get_table_status(store_name)

    return context


def get_store_names_db():
    store_names = stores.getDB.get_store_names()

    return store_names


def update_table_status(store_name, table_number, set_status, modified_number, if_modified):
    stores.updateDB.set_table_status(store_name, table_number, set_status, modified_number, if_modified)
