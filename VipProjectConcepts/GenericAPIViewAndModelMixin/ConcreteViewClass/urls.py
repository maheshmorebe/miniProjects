from django.urls import path
from . import views

urlpatterns = [
    path('studentlist/',views.StudentList.as_view()),
    path('studentretrieve/<int:pk>/', views.StudentRetrieveAPIView.as_view()),
    path('studentcreate/', views.StudentCreateAPIView.as_view()),
    path('studentupdate/<int:pk>/', views.StudentUpdateAPIView.as_view()),
    path('studentdestroy/<int:pk>/', views.StudentDestroyAPIView.as_view()),

    path('studentlistcreate/', views.StudentListCreatePIView.as_view()),
    path('studentretrieveupdate/<int:pk>/', views.StudentRetrieveUpdateAPIView.as_view()),
    path('studentretrievedestroy/<int:pk>/', views.StudentRetrieveDestroyAPIView.as_view()),
    path('studentretrieveupdatedestroy/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),

]