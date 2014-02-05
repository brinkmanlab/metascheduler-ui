from django.shortcuts import render
from django.http import Http404
from diskstats.models import diskusage
import pprint
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'diskgraph.html')
#    return HttpResponse("Hello, world. You're at the poll index.")

def fetch_roots(request):
    context = {}
    
    try:
        context['rootdirs'] = diskusage.objects.using("diskgraph").values("root_dir").distinct()
    except:
        raise Http404
    
    return render(request, "showroots.json", context, content_type='text/javascript')

def fetch_dirs(request):
    context = {}

    if request.method == 'POST':
        content = request.POST['content']
        content = json.loads(content)
        pprint.pprint(content)
        rootdir = content['rootdir']
    
    context['roodir'] = rootdir

    print rootdir


    try:
        context['dirs'] = diskusage.objects.using("diskgraph").filter(root_dir=rootdir).values("directory").order_by("directory").distinct()
    except:
        raise Http404
    
    
    
    return render(request, "showdirs.json", context, content_type='text/javascript')

def fetch_dir_set(request):
    context = {}
    
    if request.method == 'GET':
        raise Http404
    elif request.method == 'POST':
        dirset = request.POST['content']
    
    dirset = json.loads(dirset)
        
    dirs = dirset['dirs']
    size_sets = dict()
    
    context['rootdir'] = dirset['rootdir']
    
    for dir in dirs:
        set = diskusage.objects.using("diskgraph").filter(root_dir=dirset['rootdir']).filter(directory=dir).order_by('checkdate').all()
        size_sets[dir] = set
        
    context['sets'] = size_sets
       
    return render(request, "dirset.json", context, content_type='text/javascript')

# Create your views here.
