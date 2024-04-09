from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from ..models import Order
from ..serializers import OrderSerializer

# Create your views here.

# Order CRUD View
class GetOrders(generics.ListAPIView):
    # Get Request (View Orders)
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()

        # Get query parameters from the request
        customer_id = self.request.query_params.get('customer_id', None)
        status = self.request.query_params.get('status', None)

        # Filter queryset based on query parameters
        if customer_id is not None:
            queryset = queryset.filter(customer_id=customer_id)

        # For view order history
        if status in ['Delivered', 'Failed to deliver']:
            queryset = queryset.filter(status=status)
    
        return queryset

class CreateOrder(generics.CreateAPIView):
    # Post Request (Place Order)
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # Check if the order was successfully created
        success = True  # Assuming the order creation is successful
        message = "Order placed successfully." if success else "Failed to place order."
        
        return Response({"message": message, "success": success}, status=status.HTTP_201_CREATED, headers=headers)
    
class UpdateOrder(generics.RetrieveUpdateAPIView):
    # Get/Put Request (Modify Orders)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        status_before_update = instance.status

        self.perform_update(serializer)

        if status_before_update != "On the way" and instance.status == "On the way":
            print("Order status changed to 'On the way'.")
            # SEND SMS NOTIFICATION HERE
            
        success = True 
        message = "Order updated successfully." if success else "Failed to update order."
        
        return Response({"message": message, "success": success})

class DeleteOrder(generics.RetrieveDestroyAPIView):
    # Delete Request (Delete Orders)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            success = True 
            message = "Order deleted successfully."
            return Response({"message": message, "success": success}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            success = False
            message = f"Failed to delete order: {str(e)}"
            return Response({"message": message, "success": success}, status=status.HTTP_400_BAD_REQUEST)
    
