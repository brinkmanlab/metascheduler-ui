from django.shortcuts import render, get_object_or_404, render_to_response
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
    
    try:
        context['jobs'] = Task.objects.select_related().all()
    except:
        raise Http404
    
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
