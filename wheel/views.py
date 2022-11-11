from django.shortcuts import render , redirect
from wheel.models import Team
from vehicle.models import car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = car.objects.order_by('-created_date').filter(is_featured=True)
    model_search = car.objects.values_list('model',flat=True).distinct()
    city_search = car.objects.values_list('city',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    type_search = car.objects.values_list('body_style',flat=True).distinct()


    data = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'type_search' : type_search,
    }
    return render(request,'index.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'about.html', data)

def serv(request):
    return render(request,'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'you have a new message from carzone.co regarding:' + subject
        message_body = 'Name: '+ name + '.Email: '+ email + '.Phone: '+ phone + '.Message: ' + message 

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
 
        send_mail(
            'New Car Inquiry' + email_subject ,
            message_body,
            'muhammadanusimran@gmail.com',
            [admin_email],
            fail_silently = False,
        )
        messages.success(request, 'Thankyou for contacting us, our representative will get to you soon')
        return redirect('cont')

    return render(request, 'contact.html')