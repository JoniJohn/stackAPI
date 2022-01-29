from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# import controllers.summary as summary
import controllers.questions as questions

# Create your views here.
def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = {
        "question_count": questions.get_count(),
        "question_tags": questions.get_tags(),
        "question_answered": questions.is_answered_data(),
    }
    return HttpResponse(template.render(context, request))
