

from itertools import product
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from library_api import serializers
from library_api import models
from rest_framework.authentication import TokenAuthentication
from library_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.decorators import api_view


class UserSignupViewset(viewsets.ModelViewSet):                                       
    """Handel creating and updating profiles"""

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    # authentication_classes=(TokenAuthentication,)
    


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentications tokens"""

    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class AddbooksViewSet(viewsets.ModelViewSet):
    Authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.AddBooksSerializer
    queryset=models.AddBooks.objects.all()

    permission_classes=(
        permissions.Updatebookslist,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self,seralizer):
        """Set the user profile to the logged in the user"""
        seralizer.save(user_profile=self.request.user)

# @api_view('GET')
# def student(request):      
    
#     serializer=booklistSerializer.(instance=product,data=request.data) 
    
#     return Response()


def home(request):
   return render(request,'index.html')

def login(request):
   return render(request,'login.html')

def signup(request):
   return render(request,'signup.html')