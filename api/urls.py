from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt


from . import views

urlpatterns = [
	path('rest-auth/', include('rest_auth.urls')),
	path('register/', views.UserCreate.as_view(), name="account-create"),
	path('students/',views.StudentList.as_view(),name="students_list"),
	path('students/<int:pk>',views.StudentDetail.as_view(), name="students_detail")
]