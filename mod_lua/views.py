from rest_framework import generics
from .serializers import CallSerializer
from .models import Call
from rest_framework import generics, status
from rest_framework.response import Response

class CreateCall(generics.CreateAPIView):
    serializer_class = CallSerializer


class UpdateCall(generics.UpdateAPIView):
    serializer_class = CallSerializer
    
    def partial_update(self, request, pk=None):
        call = Call.objects.get(uuid=request.data['uuid'])
        serialized = CallSerializer(call, data=request.data, partial=True)
        serialized.is_valid()
        serialized.save()
        return Response(serialized.data)
