from django.http import HttpResponse
from django.shortcuts import render
from .models import Bb, Rubric

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric_id=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/rubric_bbs.html', context)










