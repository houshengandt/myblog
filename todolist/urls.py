from django.conf.urls import url

from todolist import views

urlpatterns = [
    url(r'^$', views.to_do_list_index, name='todolistindex'),
    url(r'^add-task/', views.AddTaskView.as_view(), name='add_task'),
    url(r'^create-task/', views.create_task, name='create_task'),
    url(r'^delete-task/(?P<pk>\d+)/$', views.delete_task, name='delete_task'),
    url(r'^complete-task/$', views.complete_task, name='complete_task'),
    url(r'^uncomplete-task/$', views.uncomplete_task, name='uncomplete_task'),
    url(r'^sign-in/$', views.SignInView.as_view(), name='todolistsignin'),
    url(r'^login/$', views.login_to_to_do_list, name='todolistlogin'),
    url(r'^logout/$', views.logout_off_to_do_list, name='todolistlogout'),
]
