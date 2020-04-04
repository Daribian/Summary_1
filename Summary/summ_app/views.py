from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings

from .forms import UserForm

def indexLite(request):
    if request.method == 'GET':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            firstname= form.cleaned_data['Имя']
            lastname= form.cleaned_data['Фамилия']
            emailvalue= form.cleaned_data['email']
            try:
                send_mail(firstname, lastname, settings.EMAIL_HOST_USER, ['daribian@list.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'index.html', {'form': form})

def successView(request):
    return HttpResponse('Success!')