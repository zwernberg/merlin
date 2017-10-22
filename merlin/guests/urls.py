from django.conf.urls import url

from merlin.guests import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.GuestListView.as_view(),
        name='list'
    ),
]
