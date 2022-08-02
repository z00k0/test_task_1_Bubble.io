import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from dotenv import load_dotenv

from .models import Automobile
from .forms import AutoForm
from .servises import send_message

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
chat_id = os.getenv('CHAT_ID')


def index(request):
    automobiles = Automobile.objects.all()
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            new_automobile = form.save()
            resp = send_message(new_automobile, chat_id=chat_id)
            return HttpResponseRedirect('index')
        else:
            return render(request, 'auto/index.html', {
                'automobiles': automobiles,
                'form': form,
            })
    else:
        return render(request, 'auto/index.html', {
            'automobiles': automobiles,
            'form': AutoForm(),
        })
