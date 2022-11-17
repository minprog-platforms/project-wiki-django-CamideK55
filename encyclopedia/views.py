from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    return render(request, "encyclopedia/create.html", {
    })

def wiki(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/wiki.html", {
        "content": markdown(content),
        "title": title
    })
