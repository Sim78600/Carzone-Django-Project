from django.shortcuts import render,get_object_or_404
from vehicle.models import car
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator

# Create your views here.

def cars(request):
    Cars = car.objects.order_by('-created_date')
    paginator = Paginator(Cars,1)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = car.objects.values_list('model',flat=True).distinct()
    city_search = car.objects.values_list('city',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    type_search = car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'Cars' : paged_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'type_search' : type_search,
        
    }
    return render(request,'cars.html',data)

def car_detail(request,id):
    single_car = get_object_or_404(car,pk=id)
    data = {
        'single_car' : single_car,
    }
    return render(request,'car_details.html',data)

def search(request):
    cars = car.objects.order_by('-created_date')
    model_search = car.objects.values_list('model',flat=True).distinct()
    city_search = car.objects.values_list('city',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    type_search = car.objects.values_list('body_style',flat=True).distinct()

    if 'search' in request.GET:
        search = request.GET['search']
        if search:
            cars = cars.filter(description__icontains=search)
    
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)
    
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            cars = cars.filter(body_style__iexact=type)
    
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price,price__lte=max_price)

    data = {
        'cars' : cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'type_search' : type_search,
    }
    return render(request,'search.html',data)
