from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    response = f"You're looking at result of question {question_id}."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
