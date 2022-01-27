from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import controllers.summary as summary

# Create your views here.
def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = {
        "counts": summary.get_counts()
    }
    return HttpResponse(template.render(context, request))
