from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.http import Http404
from webui.models import Task, Component, Mail
from metasched import pipeline
import pprint

# Create your views here.

def index(request):
    return render(request, 'index.html')
#    return HttpResponse("Hello, world. You're at the poll index.")

def showjobs(request):
    
    return render(request, 'showjobs.html')
     
def showjobsjson(request):
    context = {}

    context['sEcho'] = 1
    if(request.GET.get('sEcho')):
        sEcho = request.GET.get('sEcho')
        if not sEcho.isdigit():
            return HttpResponse(status=400)

 #       print "Setting secho to: " + sEcho
        context['sEcho'] = int(sEcho)

    startAt = 0
    if(request.GET.get('iDisplayStart')):
        startAt = request.GET.get('iDisplayStart')
        try:
            int(startAt)
        except ValueError:
            return HttpResponse(status=400)

        startAt = int(startAt)

    toShow = 30
    if(request.GET.get('iDisplayLength')):
        try:
            int(request.GET.get('iDisplayLength'))
        except ValueError:
            return HttpResponse(status=400)

        iDisplayLength = int(request.GET.get('iDisplayLength'))
        if iDisplayLength > 0:
            toShow = iDisplayLength

        toShow = int(toShow)

    endAt = startAt + toShow
    
    try:
        jobs = Task.objects.select_related().order_by('-task_id').all()
        context['records'] = len(jobs)
    except:
        raise Http404
    
    context['jobs'] = jobs[startAt:endAt]


    return render(request, "showjobs.json", context, content_type='text/javascript')

def jobdetails(request, job_id):
    
    return render(request, 'index.html')

def jobdetailsjson(request, job_id):
    context = {}

    try:
        context['task'] = Task.objects.select_related().get(pk=job_id)
    except:
        raise Http404
     
    pipeline_reader = pipeline.Parser()
    pipeline_data = pipeline_reader.read(context['task'].job_type)

    component_order = []
    for c in pipeline_data['components']:
        component_order.append(c['name'])
        
    context['component_order'] = component_order
#    print context['task']['job_type']
    
    return render(request, "jobdetails.json", context, content_type='text/javascript')
