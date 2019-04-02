from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Schedule
from django.core.mail import EmailMessage
import datetime

def index(request):

    update_val = ""
    if "flag" in request.session:
        flag = 1
        del request.session['flag']
    else:
        flag = 0
    if "deleted" in request.session:
        deleted = 1
        del request.session['deleted']
    else:
        deleted = 0
    if "update" in request.session:
        update = 1
        update_val = request.session['update']
        del request.session['update']
    else:
        update = 0
    todo = Schedule.objects.all()

    # Below Code is written for Mailing the user if he/she has any appointments today.
    # It is commented since we need to configure the smtp server while deploying. Once
    # it is done we can uncomment the below code and use it to send email to users.
    
    # if "email" in request.session:
    #     all_date = Schedule.objects.all().values_list('schedule_date','title')
    #     for i in all_date:
    #         print(i)
    #         if str(i[0].strftime('%Y-%m-%d'))==str(datetime.datetime.now().date()):
    #             pass
    #             email = EmailMessage('ToDo', i[1], to=[request.session["email"]])
    #             email.send()
    return render(request,"index.html",{"flag":flag,"todo":todo,"deleted":deleted,"update_val":update_val,"update":update})

def create_schedule(request):
    if request.method == "POST":
        print("Hello")
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        p = Schedule(title=title,desc=desc,schedule_date=date)
        p.save()
        request.session['flag'] = 1
    return HttpResponseRedirect(reverse('index'))

def delete_schedule(request):
    id = request.POST.get("id")
    Schedule.objects.filter(id=id).delete()
    request.session['deleted'] = 1
    return HttpResponseRedirect(reverse('index'))

def update_schedule(request):
    id = request.POST.get("id")
    request.session["post_id"] = id
    data = Schedule.objects.filter(id=id).values_list("title",'desc',"schedule_date")
    print(data[0][2])
    return render(request,"update.html",{"title":data[0][0],"date":data[0][2],"desc":data[0][1]})

def update_schedule_complete(request):
    if request.method == "POST":
        id = request.session['post_id']
        title = request.POST.get("title")
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        Schedule.objects.filter(id = id).update(title=title,desc=desc,schedule_date=date)
        del request.session['post_id']
        request.session['update'] = title
    return HttpResponseRedirect(reverse('index'))

def submit_email(request):
    request.session["email"] = request.POST.get("email")
    print(request.session["email"])
    return HttpResponseRedirect(reverse('index'))