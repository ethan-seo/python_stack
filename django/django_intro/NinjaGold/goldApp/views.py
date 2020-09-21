from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    locations = {
        "farm": (10,20),
        "cave": (5,10),
        "house": (2,5),
        "casino": (0,50)
    }
    location_name = request.POST['location']
    location = locations[location_name]
    money_change = random.randint(location[0],location[1])
    timenow = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if location_name == 'casino':
        if random.random() < 0.5:
            result = "taken"
            request.session['gold'] -= money_change
            activitylog = f"Entered a casino and lost {money_change} golds... Ouch.. ({timenow})"
        else:
            result = "earned"
            request.session['gold'] += money_change
            activitylog = f"Earned {money_change} from the {location_name}! ({timenow})"
    else:
        result = "earned"
        request.session['gold'] += money_change
        activitylog = f"Earned {money_change} from the {location_name}! ({timenow})"
    request.session['activities'].append({"activitylog": activitylog, "result": result})  
    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')