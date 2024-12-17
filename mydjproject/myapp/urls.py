from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage),
    path('home',views.homepage),
    path('home/ahmedabad',views.homepageahmedabad),
    path('home/surat',views.homepagesurat),
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('test',views.testpage),
    path('form',views.formpageview),
    path('process',views.formpageprocess),
    path('marksheet',views.marksheetview),
    path('processmsheet',views.marksheetprocess),
    path("add-student",views.addstudent),
    path("display-student",views.displaystudent),
]
