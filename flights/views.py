from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import ListSerializer,ListSerializerbooking
from datetime import datetime



class ListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListSerializer

class Booking(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today())
    serializer_class = ListSerializerbooking
