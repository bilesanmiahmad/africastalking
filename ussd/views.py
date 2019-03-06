from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
@csrf_exempt
def talk(request):
    session_id = request.POST['sessionId']
    service_code = request.POST['serviceCode']
    phone = request.POST['phoneNumber']
    text = request.POST['text']

    if text == "":
        response = "CON Welcome to my Africa's Talking USSD tutorial \n"
        response += "1. I would like to learn how to use the USSD platform \n"
        response += "2. I just want to hang out with Ahmad"
    elif text == "1":
        response = "CON Awesome lets just follow through with the tutorial"
    elif text == "2":
        response = "END Awesome, i have your number and I will give you a call soon."
    
    return HttpResponse(response, content_type='text/plain')
