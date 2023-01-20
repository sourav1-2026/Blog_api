from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BlogSerializer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
from django.db.models import Q
 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import BlogModel

    
# check the blog add post method
class BlogView(APIView):
    
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get(self,request):
        try:
            blogs=BlogModel.objects.filter(user=request.user)

            if request.GET.get('search'):
                search=request.GET.get('search')
                blogs=blogs.filter(Q(title__icontains=search) | Q(blog_text__icontains=search))


            serializer=BlogSerializer(blogs, many=True)
            return Response({
                'data':serializer.data,
                'message':'blogs fetched successfully'
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


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

    def patch(self,request):
        try:
            data=request.data
            blog=BlogModel.objects.get(uid=data.get('uid'))
            if blog==None:
                return Response({
                    'data':{},
                    'message':'Invalid blog uid'
                },status=status.HTTP_400_BAD_REQUEST)
            
            if request.user != blog.user:
                return Response({
                    'data':{},
                    'message':'you are not authorized to this'
                },status=status.HTTP_400_BAD_REQUEST)

            serializer=BlogSerializer(blog,data=data,partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request):
        try:
            data=request.data
            blog=BlogModel.objects.get(uid=data.get('uid'))
            print("delete1")
            if blog==None:
                return Response({
                    'data':{},
                    'message':'Invalid blog uid'
                },status=status.HTTP_400_BAD_REQUEST)
            print("delete2")
            if request.user != blog.user:
                return Response({
                    'data':{},
                    'message':'you are not authorized to this'
                },status=status.HTTP_400_BAD_REQUEST)
            print("delete3")
            blog.delete()
            print("delete4")
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
             return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
