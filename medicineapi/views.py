from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
from django.contrib.auth import authenticate
from medicine.forms import MedicinesForm
from .serializers import MedicinesSerializer
from medicine.models import Medicines
from django.shortcuts import get_object_or_404


# api signup

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

# api login

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)

# api create

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_medicine(request):
    form = MedicinesForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

# api read

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_medicine(request):
    medicine = Medicines.objects.all()
    serializer = MedicinesSerializer(medicine, many=True)
    return Response(serializer.data)


# api update

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_medicine(request, pk):
    medicine = get_object_or_404(Medicines, pk=pk)
    form = MedicinesForm(request.data, instance=medicine)
    if form.is_valid():
        form.save()
        serializer = MedicinesSerializer(medicine)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# api delete
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_medicine(request, pk):
    try:
        medicine = Medicines.objects.get(pk=pk)
    except Medicines.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    medicine.delete()
    return Response("deleted successfully")

# api search

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_medicine(request):
    medicine_name = request.query_params.get('name', None)
    if medicine_name is not None:
        medicine = Medicines.objects.filter(name__icontains=medicine_name)
        if medicine.exists():
            serializer = MedicinesSerializer(medicine, many=True)
            return Response(serializer.data)
        else:
            return Response({'message':'no medicine found for given name'},status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'message':'please enter a name'},status=status.HTTP_400_BAD_REQUEST)
    




