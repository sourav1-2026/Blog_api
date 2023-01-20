from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserRegisterSerializer,LoginSerializer
from rest_framework import status
#from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.

class UserRegisterView(APIView):

    def get(self, request): 
        #Return a list of all users.
        return Response({
            'msg':"get request"
        })

    def post(self, request):
        try:
            data=request.data
            serializer=UserRegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                #print("Serializer data {}".format(serializer.data))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                # In Response we are passing Json
                # serializer.data is a josn which we break as validated data
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            if serializer.is_valid():
                response=serializer.get_tokens_for_user(serializer.data)
                return Response(response, status=status.HTTP_200_OK)
            return Response({'message':'not able to generate the token'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong to connect'
            },status=status.HTTP_400_BAD_REQUEST)


                

# class UserRegisterView(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserRegisterSerializer


