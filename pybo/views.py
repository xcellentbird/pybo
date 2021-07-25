from pybo.models import Question
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Question
from django.utils import timezone


def index(request):
    """
    pybo 목록 출력
    """
    # question 모델 데이터를 작성 날짜 역순으로 정렬
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # return HttpResponse('<h1>안녕하세요 pybo에 오신 것을 환영합니다</h1>')
    return render(request, 'question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'question_detail.html', context)


def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get(
        'content'), create_date=timezone.now())

    return redirect('detail', question_id=question_id)
