from django.urls import path
from .views import *
urlpatterns = [
    path('jobs/',job_list , name='job_list'),
    path('',employee_list , name='employee_list'),
    path('create/',EmployeeCreateStoreView.as_view() , name='employee_create'),
    # path('store/',employee_store , name='employee_store'),
    path('<int:pk>/',EmployeeDetailView.as_view() , name='employee_info'),
    path('<int:id>/delete',UpdateDeleteEmployeeView.as_view() , name='employee_action'),
    path('<int:id>/delete/',employee_delete , name='employee_delete'),
]
