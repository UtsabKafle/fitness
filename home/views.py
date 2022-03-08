from pydoc import render_doc
import re
from unicodedata import name
from django.shortcuts import render
from django.test import RequestFactory
from numpy import full
from .models import workout,instruction,images,rep,set,routine,date,data
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from pynput.keyboard import Controller,Key
from datetime import date as dt
keyboard = Controller()
# Create your views here.
def return_name(i):
    xx = set.objects.filter(day=i)
    listd = {}
    for i in xx:
        listd[i.name]=i.id
    return listd

def dashboard(request):
    all_days = routine.objects.all()
    # date_ = date.objects.create()
    da = []
    for i in all_days:
        da.append({'day':i.day,'id':i.id,'workouts':return_name(i)})
    context = {
        'days':da,
        
    }
    return render(request,'home/dashboard/dashboard.html',context)

def sets(request):
    all_sets = set.objects.all()
    context = {
        'sets':all_sets
    }
    return render(request,'home/dashboard/sets.html',context)

def return_workout_name(i):
    xx = workout.objects.filter(set=i)
    listd = {}
    for i in xx:
        listd[i.name]=i.id
    return listd

def sets_view(request,id):
    routine_ = routine.objects.get(id=id)
    set_ = set.objects.filter(day=routine_)
    workouts = workout.objects.filter(set=set_)
    all = []
    for i in set_:
        all.append({'set':i.name,'id':i.id,'workouts':return_workout_name(i)})
    context={
        'all':all,
        'day':routine_.day
    }
    return render(request,'home/dashboard/sets_view.html',context)


def set_detailed_view(request,id):
    set_ = set.objects.get(id=id)
    workouts = workout.objects.filter(set=set_)
    if request.method == "POST":
        try:
            date_ = date.objects.get(date=dt.today())
        except ObjectDoesNotExist:
            date_ = date.objects.create()
        data_ = data.objects.create(set=set_,day=date_)
    context = {
        'set':set_,
        'workouts':workouts
    }
    return render(request,'home/dashboard/set_detailed_view.html',context)


def workout_view(request,id):
    workout_ = workout.objects.get(id=id)
    try:
        images_ = images.objects.get(workout=workout_)
    except ObjectDoesNotExist:
        images_ = None
    instructions = instruction.objects.filter(workout=workout_)
    if request.method == "POST":
        reps_ = request.POST['reps']
        rep_ = rep.objects.create(workout=workout_,reps=reps_)
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release(Key.ctrl)
    context = {
        'workout':workout_,
        'image':images_,
        'instructions':instructions

    }
    return render(request,'home/workout/workout_view.html',context)

def do_shit(data):
    cont = []
    reps_ = rep.objects.filter(workout=data)
    for i in reps_:
        cont.append(int(i.reps))
    print(cont)
    return int(sum(cont))

def me_view(request):
    dates = date.objects.all()
    workouts = workout.objects.all()
    dates_=[]
    total_sets = []
    a_rep = []
    for i in workouts: 
        a_rep.append({'workout':i.name,'reps':do_shit(i)})
    all_reps = rep.objects.all()
    total_reps = []
    for i in all_reps:
        val = i.reps
        total_reps.append(int(val))
    for i in dates:
        full_date = str(i.date)
        year = full_date.split('-')[0]
        month = full_date.split('-')[1]
        day = full_date.split('-')[2]
        dates_.append({'month':int(month),'day':day,'year':year})
        datas = data.objects.filter(day=i)
        for data_ in datas:
            total_sets.append(data_.set.name)
    context={
        'dates':dates_,
        'total_days':dates.count(),
        'all_workouts':workouts,
        'all':a_rep,
        'total_reps':sum(total_reps),
        'total_workouts':workouts.count()

        
    }
    return render(request,'me/me.html',context)


def date_workout_view(request,id):
    get_date = date.objects.filter(date=id)
    workouts_list = []
    for i in get_date:
        datas = data.objects.filter(day=i)
        for i_ in datas:
            workouts = workout.objects.filter(set=i_.set)
            for j in workouts:
                reps = rep.objects.filter(workout=j)
                for i__ in reps:
                    _d = {'workout':j.name,'reps':i__.reps}
                    if _d not in workouts_list:
                        workouts_list.append(_d)
    context={
        'workout_list':workouts_list
    }
    return render(request,'me/date_workout_view.html',context)


def transformation_view(request):
    #picform = PictureForm()
    picform = PictureForm(request.POST or None, request.FILES or None)
    if picform.is_valid():
        picform.save()
    imgs = transformation.objects.all()
    
    context = {
        'form':picform,
        'images':reversed(imgs)
    }
    return render(request,'home/transformation/transformation_view.html',context)