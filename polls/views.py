from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	template_dir = 'polls/index.html'
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, template_dir, context)

def more_info(request):
	return HttpResponse("<h1>Over here we are starting with django and we gonna build a polls app. Stay tuned...</h1>")

def detail(request, question_id):
	template_dir = 'polls/detail.html'
	question = get_object_or_404(Question, pk=question_id)
	context = {
		'question': question,
	}
	return render(request, template_dir, context)

def results(request, question_id):
	template_dir = 'polls/results.html'
	question = get_object_or_404(Question, pk=question_id)
	context = {
		'question': question,
	}
	return render(request, template_dir, context)

def vote(request, question_id):
	template_dir = 'polls/detail.html'
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, template_dir, {
			'error_message': "You didn't select a choice.", 'question': question,
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))