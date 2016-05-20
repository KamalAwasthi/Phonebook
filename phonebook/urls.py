from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact_list, name='contact_list'),
    url(r'^contact_detail/(?P<pk>\d+)/$', views.contact_detail, name='contact_detail'),
    url(r'^Add_New$', views.Add_New, name='Add_New'),
    url(r'^edit_contact/(?P<pk>\d+)/$', views.contact_edit, name='contact_edit'),
    url(r'^contact_delete/(?P<pk>\d+)/$', views.contact_delete, name='contact_delete'),
    url(r'^get_data$',views.list,name='list'),
]
