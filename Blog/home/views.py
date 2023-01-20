from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BlogSerializer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

    
# check the blog add post method
class BlogView(APIView):
    
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def post(self,request):
        try:
            data=request.data
            data['user']=request.user.id
            print(data)
            # print(request.user.id)
            # print(request.user)
            serializer=BlogSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                {
                'data':serializer.data,
                'message':"blog created succesfull"
                }, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
        except Exception as e:
           return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)