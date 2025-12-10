from django.shortcuts import render
def mileage(request):
    d=int(request.POST.get('distance', 0))
    f=int(request.POST.get('fuel', 0))
    m= d/f if request.method == 'POST' and f!=0 else 0
    print("The Total Distance Traveled:",d)
    print("Fuel used:",f)
    print("Mileage",m)
    return render(request, 'mathapp/math.html', {'d': d, 'f': f, 'm': m})

