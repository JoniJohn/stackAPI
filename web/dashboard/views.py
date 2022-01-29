from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from controllers import questions, articles, posts

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
        "articles_count": articles.get_count(),
        "article_tags": articles.get_tags()
    }
    return HttpResponse(template.render(context, request))

# Posts dashboard
def dashboard3(request):
    template = loader.get_template('dashboard3.html')
    context = {
        "post_activity": posts.get_count(),
    }
    return HttpResponse(template.render(context, request))
