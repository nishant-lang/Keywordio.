
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from library_api import views

router=DefaultRouter()

router.register('signupapi',views.UserSignupViewset),
router.register('addbook',views.AddbooksViewSet,)

urlpatterns = [
  
    path('loginapi/',views.UserLoginApiView.as_view()),
    # path('student',views.StudentViewSet.as_view()),
    path('',include(router.urls)),
    path('index/', views.home, name="index.html"),
    path('login/', views.login, name="login.html"),
    path('signup/', views.signup, name="signup.html"),
]