from . import views
from django.urls import path



urlpatterns = [
    #add add task feature
    path('addtask/',views.addtask,name='addtask'),
    
    #mark as done feature
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    
    #mark as undone feature
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),

    #edit feature
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),

    #delete feature
    path('delete_task/<int:pk>/',views.delete_task,name="delete_task"),
]
