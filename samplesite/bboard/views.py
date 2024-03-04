from django.http import HttpResponse
from django.shortcuts import render
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from.forms import BbForm


#Функция главной страницы с объявлениями.
def index(request):
    """Функция получает данные из модели,
    передает их через контекст в шаблоны"""
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


#Функция страниц с разделением на рубрики.
def rubric_bbs(request, rubric_id):
    """Функция получает, фильтрует данные из моделей
     Отдает данные в шаблоны через контекст"""
    bbs = Bb.objects.filter(rubric_id=rubric_id) #вывод объявлений принадлежащих рубрике.
    rubrics = Rubric.objects.all()               #Получение всех рубрик для отображения.
    current_rubric = Rubric.objects.get(pk=rubric_id) #вывод конректной рубрики на странице.
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/rubric_bbs.html', context)

#
class BbCreateView(CreateView):
    """Класс для обработки формы BbForm."""
    template_name = 'bboard/bb_create.html'
    form_class = BbForm
    success_url = '/bboard/'

    def get_context_data(self, **kwargs):
        """Переопределим метод из род.класса для вывода
         на странице формы  - списка рубрик"""
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context














