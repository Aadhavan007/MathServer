# Ex.04 Design a Website for Server Side Processing
## Date:10-12-2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html

<html>
    <head>
        <title>Mileage Calculator</title>
        <link href="style.css" rel="stylesheet">
        <style>
            .box
            {
                width: 500px;
                height: 500px;
                background-color: black;
                position: fixed;
                top: 130px;
                left: 510px;
                text-align:center;
                
            }
            
        </style>
    </head>
    <body>
        <div class="box">
            <font color="white"><h1 align="center">MILEAGE CALCULATOR</h1> </font>
            <font color="white"><h2 align="center">M AADHAVAN NAGARAJAN 25011373</h2></font>
            <hr color="lime"> 

            <form method="post">
                {% csrf_token %}
                <br>
                <br>
                <font color="white" size="5"> <label>The Total Distance Traveled:<label></font>
                <input type="number" name="distance" value="{{d}}">
                <br>
                <br>
                <br>
                <font color="white" size="5"> <label>Fuel Consumed:</label></font>
                <input type="number" name="fuel" value="{{f}}">
                <br>
                <br>
                <br>
                <button type="submit">Calculate</button>
                <br>
                <br>
                <br>
                <font color="white" size="5"> <label>Mileage:</label></font>
                <input class='result' type="number" name="Mileage" value="{{m}}">

            </form>
            

        </div>
    </body>
</html>

views.py

from django.shortcuts import render
def mileage(request):
    d=int(request.POST.get('distance', 0))
    f=int(request.POST.get('fuel', 0))
    m= d/f if request.method == 'POST' and f!=0 else 0
    print("The Total Distance Traveled:",d)
    print("Fuel used:",f)
    print("Mileage",m)
    return render(request, 'mathapp/math.html', {'d': d, 'f': f, 'm': m})

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [path('', views.mileage, name='mileage')]

```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (79).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (81).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
