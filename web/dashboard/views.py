from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# import controllers.summary as summary
import controllers.questions as questions
import controllers.articles as articles

# Questions dashboard
def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = {
        "question_count": questions.get_count(),
        "question_tags": questions.get_tags(),
        "question_answered": questions.is_answered_data(),
    }
    return HttpResponse(template.render(context, request))

# Articles dashboard
def dashboard2(request):
    template = loader.get_template('dashboard2.html')
    context = {
        "articles_count": articles.get_count()
    }
    return HttpResponse(template.render(context, request))
