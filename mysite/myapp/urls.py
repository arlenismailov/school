from .views import EventsView, TeacherView, PhotoEventsView
from django.urls import path

urlpatterns = [
    path('events/', EventsView.as_view({'get': 'list', 'post': 'create'}), name='events_list'),
    path('event/<int:pk>/', EventsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='event_detail'),

    path('teachers/', TeacherView.as_view({'get': 'list', 'post': 'create'}), name='teachers_list'),
    path('teacher/<int:pk>/', TeacherView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='teacher_detail'),

    path('photo_events/', PhotoEventsView.as_view({'get': 'list', 'post': 'create'}),
         name='photo_list'),
    path('photo_events/<int:pk>/', PhotoEventsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='photo_detail'),
]
