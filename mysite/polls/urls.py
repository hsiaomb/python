from django.conf.urls import url

from . import views

app_name = "polls"
urlpatterns = [
	# This will display: /polls/
	url(r'^$', views.IndexView.as_view(), name = "index"),
	# This will display: /polls/5
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
	# This will display /polls/5/results/
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = "results"),
	# This will display: /polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = "vote")
]
