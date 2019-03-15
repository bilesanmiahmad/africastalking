from rest_framework.serializers import ModelSerializer
from ussd.models import UserData

class RequestSerializer(ModelSerializer):

    class Meta:
        model = UserData
        fields = [
            'id', 'crop', 'bags', 'pickup',
            'destination', 'mobile_money'
        ]