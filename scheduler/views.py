from django.shortcuts import render, redirect
from .forms import UserRegisterForm, CustomUserForm, ScheduleForm
from .models import Schedule

import platform, subprocess

# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()        
        context['form'] = form
    return render(request, 'scheduler/home.html', context)


def valid_ip(ip):
    if len(ip) > 16:
        return False
    strarr = ip.split('.')
    arr = [int(numeric_string) for numeric_string in strarr]
    if len(arr) != 4:
        return False
    for x in arr:
        if x < 0 or x > 255:
            return False
    return True

def ping(host):
  
    param = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0
    
def schedule(request):
    context = {}
    context['schedules'] = Schedule.objects.all()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        context['form'] = form
        if form.is_valid():
            ip = form.cleaned_data.get('IP')
            if valid_ip(ip):
                context['valid'] = True
                form.save()
                hostTrue = ping(ip)
                print(hostTrue)
                context['hostTrue'] = hostTrue
            else:
                context['valid'] = False

    else:
        form = ScheduleForm()
        context['form'] = form
    return render(request, 'scheduler/schedule.html', context)


def ping_detail(request, pk):
    ip = Schedule.objects.all().get(id = pk)
    print(ip.IP)
    context = {}
    context['ip'] = ip
    ping_return_value = ping(ip.IP)
    context['ping_return_value'] = ping_return_value
    
    return render(request, 'scheduler/detail.html', context)