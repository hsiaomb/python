from django.conf.urls import url
from . import views


urlpatterns = [
	# This will display: /polls/
	url(r'^$', views.index, name = "index"),
	# This will display: /polls/5
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = "detail"),
	# This will display /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = "results"),
	# This will display: /polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = "vote")
]
