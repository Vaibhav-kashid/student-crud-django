from django.urls import path
from . import views 

urlpatterns = [
    path('student/',views.student),
    path('add/',views.add_student),
    path('edit/<int:id>/',views.edit_student),
    path('del/<int:id>/',views.del_student),
]