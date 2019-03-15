from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import action

from ussd.serializers import RequestSerializer
from ussd.models import UserData

# Create your views here.
@csrf_exempt
def talk(request):
    session_id = request.POST['sessionId']
    service_code = request.POST['serviceCode']
    phone = request.POST['phoneNumber']
    text = request.POST['text']
    crop = ""
    pickup = ""
    qty = ""
    destination = ""

    if text == "":
        response = "CON Welcome to LOOP. Choose your goods. \n"
        response += "1. Corn \n"
        response += "2. Beans \n"
        response += "3. Mix"
    elif text == "1":
        crop = 'Corn'
        response = "CON Input the quantity of bags \n"
        response += "1. Less than 10 \n"
        response += "2. Less than 20 \n"
        response += "3. Over 20"
    elif text == "1*1":
        qty = "Less than 10"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "1*2":
        qty = "Less than 20"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "1*3":
        qty = "Over 20"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "1*1*1":
        pickup = "Techiman"
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "1*1*2":
        pickup = "Somanya"
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "1*1*3":
        pickup = 'Koforidua'
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "1*1*1*1":
        destination = "Madina Market"
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "1*1*1*2":
        destination = "Makola Market"
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "1*1*1*1*1":
        phone_num = phone
        response = "END You have chosen to make payment from this number " + phone + ". Please wait for your confirmation message. Thank you."

    elif text == "2":
        crop = 'Beans'
        response = "CON Input the quantity of bags \n"
        response += "1. Less than 10 \n"
        response += "2. Less than 20 \n"
        response += "3. Over 20"
    elif text == "2*1":
        qty = "Less than 10"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "2*2":
        qty = "Less than 20"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "2*3":
        qty = "More than 20"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "2*1*1":
        pickup = "Techiman"
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "2*1*2":
        pickup = "Somanya"
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "2*1*3":
        pickup = "Koforidua"
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "2*1*1*1":
        destination = "Madina Market"
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "2*1*1*2":
        destination = "Makola Market"
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "2*1*1*1*1":
        phone_num = phone
        response = "END You have chosen to make payment from this number " + phone + ". Please wait for your confirmation message. Thank you."

    elif text == "3":
        crop = 'Mix'
        response = "CON Input the quantity of bags \n"
        response += "1. Less than 10 \n"
        response += "2. Less than 20 \n"
        response += "3. Over 20"
    elif text == "3*1":
        qty = "Less than 10"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "3*2":
        qty = "Less than 20"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "3*3":
        qty = "More than 20"
        response = "CON Select pick-up location \n"
        response += "1. Techiman \n"
        response += "2. Somanya \n"
        response += "3. Koforidua"
    elif text == "3*1*1":
        pickup = "Techiman"
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "3*1*2":
        pickup = "Somanya"
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "3*1*3":
        pickup = "Koforidua"
        response = "CON Select destination \n"
        response += "1. Madina Market \n"
        response += "2. Makola Market"
    elif text == "3*1*1*1":
        destination = "Madina Market"
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "3*1*1*2":
        destination = "Makola Market"
        response = "CON Please make a payment of () via mobile money. Select 1 to use this number or enter a number below \n"
        response += "1. This number \n"
        response += "2. Different number"
    elif text == "3*1*1*1*1":
        phone_num = phone
        response = "END You have chosen to make payment from this number " + phone + ". Please wait for your confirmation message. Thank you."
    
    phone_request = UserData.objects.create(
        crop=crop,
        bags=qty,
        pickup=pickup,
        destination=destination,
        mobile_money=phone_num
    )
    
    return HttpResponse(response, content_type='text/plain')

class RequestViewSet(ModelViewSet):
    serializer_class = RequestSerializer
    model = UserData
    permission_classes = [AllowAny,]

    @action(methods=['GET'], detail=False, url_path='get-requests')
    def get_requests(self, requests):
        requests = UserData.objects.all()
        serializer = self.serializer_class(requests, many=True)
        return Response(
            {
                'response': serializer.data
            },
            status=status.HTTP_200_OK
        )
