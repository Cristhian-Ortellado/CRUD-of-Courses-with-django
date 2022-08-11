from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('storeCourse/',views.storeCourse),
    path('editCourse/<code>',views.editCourse),
    path('updateCourse/',views.updateCourse),
    path('deleteCourse/<code>',views.deleteCourse)
]