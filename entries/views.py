from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext, loader

from entries.models import EffortInstance

# Create your views here.
def index(request):
	latest_EffortInstance_list = EffortInstance.objects.order_by('-date_start')[:5]
	template = loader.get_template('entries/index.html')
	context = RequestContext(request, {'latest_EffortInstance_list': latest_EffortInstance_list,})
	return HttpResponse(template.render(context))
    
def detail(request, entries_id):
    return HttpResponse("You're looking at entries %s." % entries_id)

def results(request, entries_id):
    return HttpResponse("You're looking at the results of entries %s." % entries_id)

def vote(request, entries_id):
    return HttpResponse("You're voting on entries %s." % entries_id)
