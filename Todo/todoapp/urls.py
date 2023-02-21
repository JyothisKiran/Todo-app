from django.urls import path
from .views import TaskView,Taskcreate,Taskupdate,Taskdelete,Taskdetail,signup,signin,home



urlpatterns = [
    path('',home,name='home'),
    path('list/',TaskView.as_view(),name = 'items'),
    path('create/',Taskcreate.as_view(),name ='create_items'),
    path('update/<int:pk>',Taskupdate.as_view(),name ='update_items'),
    path('delete/<int:pk>',Taskdelete.as_view(),name ='delete_items'),
    path('details/<int:pk>',Taskdetail.as_view(),name ='detail_items'),
    # path('login/',CustomLoginView.as_view(),name = 'login'),
    path('register/',signup,name='signup'),
    path('signin/',signin,name ='signin'),

]