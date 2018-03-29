from rest_framework.response import Response
from rest_framework.views import APIView

from protect.core.api.serializer import PersonSerializer
from protect.core.models import Person


class ApiPersons(APIView):
    serializer_class = PersonSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Person.objects.filter(is_active=True).order_by('-created'), context={"request": request},
                                           many=True)
        return Response(serializer.data)
