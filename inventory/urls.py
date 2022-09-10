from django.urls import path
from . import views
urlpatterns = [
  path('',views.index,name='index'),
  path('display_laptops',views.display_laptops,name='display_laptops'),
  path('display_desktop',views.display_desktop,name='display_desktop'),
  path('display_mobile',views.display_mobile,name='display_mobile'),
  path('add_laptop',views.add_laptop,name='add_laptop'),
   path('add_desktop',views.add_desktop,name='add_desktop'),
   path('add_mobile',views.add_mobile,name='add_mobile'),
   path('edit_laptop/<venue_id>)',views.edit_laptop,name='edit_laptop'),
   path('edit_desktop/<venue_id>)',views.edit_desktop,name='edit_desktop'),
   path('edit_mobile/<venue_id>)',views.edit_mobile,name='edit_mobile'),
    path('delete_laptop/<venue_id>)',views.delete_laptop,name='delete_laptop'),
    path('delete_desktop/<venue_id>)',views.delete_desktop,name='delete_desktop'),
     path('delete_mobile/<venue_id>)',views.delete_mobile,name='delete_mobile'),
   #path('edit_laptop/(?P<pk>\d+)',views.edit_laptop,name='edit_laptop'),
   #path('edit_desktop/(?P<pk>\d+',views.edit_desktop,name='edit_desktop'),
   #path('edit_mobile/(?P<pk>\d+',views.edit_mobile,name='edit_mobile'),

  
]