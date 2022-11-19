from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown

from . import util

def index(request):
    if request.method == "POST":
        title = request.POST["q"]
        if title in util.list_entries():
            content = util.get_entry(title)
            return render(request, "encyclopedia/wiki.html", {
                "title": title,
                "content": markdown(content),
            })
        else:
            return render(request, "encyclopedia/error2.html", {
            })

    return render(request, "encyclopedia/index.html", {
    "entries": util.list_entries()
    })

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        content = "#" + title + "\n" + content

        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
            })

        util.save_entry(title, content)
        return render(request, "encyclopedia/wiki.html", {
            "content": markdown(content),
            "title": title
        })
    return render(request, "encyclopedia/create.html", {
    })

def wiki(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/wiki.html", {
        "content": markdown(content),
        "title": title
    })
