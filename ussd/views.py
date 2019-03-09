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
        response = "CON Welcome to LOOP. Choose your goods. \n"
        response += "1. Corn \n"
        response += "2. Beans \n"
        response += "3. Mix"
    elif text == "1":
        response = "CON Input the quantity of bags \n"
        response += "1. Less than 10 \n"
        response += "2. Less than 20 \n"
        response += "3. Over 20"
    elif text == "1*1":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "1*2":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "1*3":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "1*1*1":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "1*1*2":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "1*1*3":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "1*1*1*1":
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "1*1*1*2":
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "1*1*1*1*1":
        response = "END You have chosen to make payment from this number " + phone + ". Please wait for your confirmation message. Thank you."

    elif text == "2":
        response = "CON Input the quantity of bags \n"
        response += "1. Less than 10 \n"
        response += "2. Less than 20 \n"
        response += "3. Over 20"
    elif text == "2*1":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "2*2":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "2*3":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "2*1*1":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "2*1*2":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "2*1*3":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "2*1*1*1":
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "2*1*1*2":
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "2*1*1*1*1":
        response = "END You have chosen to make payment from this number " + phone + ". Please wait for your confirmation message. Thank you."

    elif text == "3":
        response = "CON Input the quantity of bags \n"
        response += "1. Less than 10 \n"
        response += "2. Less than 20 \n"
        response += "3. Over 20"
    elif text == "3*1":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "3*2":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "3*3":
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "3*1*1":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "3*1*2":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "3*1*3":
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "3*1*1*1":
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "3*1*1*2":
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "3*1*1*1*1":
        response = "END You have chosen to make payment from this number " + phone + ". Please wait for your confirmation message. Thank you."
    
    return HttpResponse(response, content_type='text/plain')
