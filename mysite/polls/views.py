from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Choice, Question


def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	#Orders the 5 latest questions
	context = {
		"latest_question_list": latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	#pk = Primary key
	#get_object_or_404: looks for object, and returns Error 404 if object does not exist.
	return render(request, 'polls/detail.html', {"question": question})

def results(request, question_id):
	response = "You're looking at the results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST["choice"])
	except (KeyError, Choice.DoesNotExist):
		return render(request, "polls/detail.html", {
			"question": question,
			"error_message": "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls/results', args=(question.id,)))
