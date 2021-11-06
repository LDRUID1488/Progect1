import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView
from .models import *


class AboutListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(AboutListView, self).get_context_data(**kwargs)
        return context


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})


def home(request):
    news = Project.objects.all()
    return render(request, "hello/home.html", {'news':news})

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request):
    return render(
        request,
        'hello/hello_there.html',
        {
            'date': datetime.now()
        }
    )

