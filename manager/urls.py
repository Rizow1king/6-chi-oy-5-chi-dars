from django.urls import path
from .views import home, courses_by_id, courses_detail
from . import views

urlpatterns = [
    path('', home, name='home_page'),
    path('course/<int:course_id>/', courses_by_id, name='courses_by_id'),
    path('courses/<int:detailed_course_id>/', views.courses_detail, name='courses_detail'),
]