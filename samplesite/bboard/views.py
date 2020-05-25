from django.http import HttpResponse
from django.template import loader
from .models import Bb
from .models import Rubric

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs':bbs}
    return HttpResponse(template.render(context, request))

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubrick_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)
