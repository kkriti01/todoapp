from django.conf.urls import url
from django.contrib.auth.views import logout


from views import todo_create, login_user, todo_list, todo_update,todo_filter, register_user

urlpatterns = [
    url(r'^todo/$', todo_create, name="index"),
    url(r'^login/$', login_user, name="login"),
    url(r'^logout/$', logout, {'next_page': '/login/'}),
    url(r'^todo_list/$', todo_list, name="todo_list"),
    url(r'^register/$', register_user, name="todo_list"),
    url(r'^todo_filter/$', todo_filter, name="todo_filter"),
    url(r'^(?P<id>[0-9]+)/update/$', todo_update, name='update'),





]
