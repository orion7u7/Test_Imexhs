from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import DeviceDataSerializer
from .models import DeviceData
import logging

logger = logging.getLogger(__name__)

# Create a viewset for the DeviceData model
class DeviceDataViewSet(viewsets.ModelViewSet):
    queryset = DeviceData.objects.all()
    serializer_class = DeviceDataSerializer

    # Override the create, update, and destroy methods to log the request data
    
    # Create a new DeviceData object
    def create(self, request, *args, **kwargs):
        logger.info(f"POST Request data: {request.data}")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            logger.info(f"POST Request success: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"POST Request failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Update an existing DeviceData object
    def update(self, request, *args, **kwargs):
        logger.info(f"PUT/PATCH Request data: {request.data}")
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            logger.info(f"PUT/PATCH Request success: {serializer.data}")
            return Response(serializer.data)
        logger.error(f"PUT/PATCH Request failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete an existing DeviceData object
    def destroy(self, request, *args, **kwargs):
        logger.info(f"DELETE Request data: {request.data}")
        instance = self.get_object()
        self.perform_destroy(instance)
        logger.info(f"DELETE Request success")
        return Response(status=status.HTTP_204_NO_CONTENT)