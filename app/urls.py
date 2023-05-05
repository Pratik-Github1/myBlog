from django.urls import path
from app import views
from .views import  GeneratePdf_Resume

urlpatterns = [
    
    path('save/' , views.saveView , name="save") ,
    path("resume/pdf" , GeneratePdf_Resume.as_view() , name="resume/pdf") ,
]
