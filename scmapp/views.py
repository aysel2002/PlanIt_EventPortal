#import django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from scmapp.models import User, Admin, Event, Book_ground,upcoming_events
import datetime

# Create your views here.

#User Registration / Login Page
def index(request):
    return render(request,'registration.html')

#User Home Page
def user_home(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}

        if 'book_status' in request.session:
            data['status'] = request.session['book_status']

        return render(request,'user_home.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'registration.html',context=data)

#User Event Page
def user_event(request):
    if 'uname' in request.session:
        event = Event.objects.all()
        data = {'event':event}
        return render(request,'user_event.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'registration.html',context=data)

#User Ground Booking Page
def ground_booking(request):
    if 'uname' in request.session:
        data = {'date':datetime.date.today()}
        return render(request,'ground_booking.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'registration.html',context=data)

#User Logout
def user_logout(request):
    if 'uname' in request.session:
        del request.session['uname']

    if 'book_status' in request.session:
        del request.session['book_status']

    return render(request,'registration.html')

#Admin Login Page
def admin_login(request):
    return render(request,'admin_login.html')

#Admin Home Page
def admin_home(request):
    if 'aname' in request.session:
        data = {'name':request.session.get('aname')}
        return render(request,'admin_home.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#Admin View Bookings
def admin_booking(request):
    if 'aname' in request.session:
        booking = Book_ground.objects.all()
        data = {'booking':booking}
        return render(request,'admin_booking.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#Admin Manage Event Page
def admin_event(request):
    if 'aname' in request.session:
        event = Event.objects.all()
        data = {'event':event}

        if 'event_status' in request.session:
            data['status'] = request.session.get('event_status')

        return render(request,'admin_event.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#Admin Update Event Page
def update_event(request,id):
    if 'aname' in request.session:
        event = Event.objects.get(eid=id)
        event.date = event.date.strftime('%Y-%m-%d')
        event.time = event.time.strftime('%H:%M:%S')
        data = {'event':event}
        return render(request,'update_event.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#Admin Add Event Page
def add_event(request):
    if 'aname' in request.session:
        return render(request,'add_event.html')
    else:
        return HttpResponse('Something went wrong')

#Admin Logout
def admin_logout(request):
    if 'aname' in request.session:
        del request.session['aname']

    if 'event_status' in request.session:
        del request.session['event_status']

    return render(request,'admin_login.html')

#BACKEND -> For User Registration
def test(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')

        if(password == re_password):
            user = User(name=name,email=email,gender=gender,password=password)
            user.save()
            request.session['uname'] = name
            return user_home(request)
        else:
            data = {'status':"Password and Re-entered password must be same"}
            return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For User Login
def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name)

            if user.password == password:
                request.session['uname'] = name
                return user_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'registration.html',context=data)

        except Exception as e:
            data = {'status':"User does not exists! You have to register first."}
            return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For Admin Login
def login_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = Admin.objects.get(name=name)

            if user.password == password:
                request.session['aname'] = name
                # return HttpResponse('ffaf')
                return admin_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'admin_login.html',context=data)

        except Exception as e:
            data = {'status':"Invalid Username"}
            return render(request,'admin_login.html',context=data)
    else:
        return HttpResponse("Something went wrong faffsffa!!!!!")

#BACKEND -> For Ground Booking
def db_ground_booking(request):
    if request.method == 'POST':
        # mobile = request.POST.get('mobile')
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        print("date--------------------- ", date)

        try:
            book = Book_ground.objects.filter(date=date)
            if book is not None:
                print(request.user.id)
                uid = int(request.user.id)
                print("date.....",date)
                book = Book_ground.objects.create(uid=uid, name=name,  date=date, time=time)

            #data = {'status':'Please select other date'}
            return render(request,'ground_booking.html',context="")
        except Exception as e:
            user = User.objects.get(name=request.session['uname'])
            book = Book_ground.objects.create(uid=user.uid,name=user.name,date=date,time=time)
            book.save()
            request.session['book_status'] = "Booking successful"
            return user_home(request)
    else:
        return HttpResponse("Something went wrong!!!!!")
#BACKEND -> For Update Event
def db_update_event(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        duration = request.POST.get('duration')

        event = Event.objects.get(eid=id)
        event.name = name
        event.date = date
        event.time = time
        event.duration = duration
        event.save()

        request.session['event_status'] = 'Event updated successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For Delete Events
def db_delete_event(request,id):
    if request.method == 'GET':
        event = Event.objects.get(eid=id)
        event.delete()

        request.session['event_status'] = 'Event deleted successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For Add Event
def db_add_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        duration = request.POST.get('duration')

        event = Event(name=name,date=date,time=time,duration=duration)
        event.save()
        request.session['event_status'] = 'Event added successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

def home(request):
    return render(request, 'home.html')
    #return HttpResponse("home page")
def upcoming(request):
    if 'uname' in request.session:
        event = upcoming_events.objects.all()
        data = {'event': event}
        return render(request, 'upcoming.html', context=data)
    else:
        data = {'status': 'You need to login first'}
        return render(request, 'registration.html', context=data)
