from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """返回最新的5个问题"""
        return Question.objects.order_by('-pub_date')[:5]


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#     # 被 render() 封装了 HttpResponse -> template 的常规流程
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return HttpResponse(f"You're looking at question {question_id}.")


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
