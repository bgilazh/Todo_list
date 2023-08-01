from django.shortcuts import render
from todo_list.models import Todo
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core import validators

notes1 = Todo.objects.all()

# Create your views here.


def index(request):
    

    if request.POST:
            noter = request.POST['note']
            new_note = Todo(note = noter)
            
            if Todo.objects.filter(note = new_note.note.lower()).exists()==False:
                new_note.save()

    notes = Todo.objects.all().values()
    #notes = Todo.objects.values_list('note',flat=True).distinct()
    print("alo alo type of notes eto ")
    print(type(notes))
    template = loader.get_template('todo_list/index.html')
    context = {
        'notes':notes,
    }
        
    
        
    #return render(request, 'todo_list/index.html', {'notes':notes1})
    return HttpResponse(template.render(context, request))
    
'''
def addrecord(request):
    noter = request.POST['note']
    new_note = Todo(note = noter)
    new_note.save()
    return HttpResponseRedirect(reverse('index'))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

    '''

def delete(request, id):
    m = Todo.objects.get(id = id)
    m.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
     m = Todo.objects.get(id = id)
     template = loader.get_template('todo_list/update.html')
     context = {
          'm':m
     }
     return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  noter = request.POST['note']
  m = Todo.objects.get(id=id)
  m.note = noter
  m.save()
  return HttpResponseRedirect(reverse('index'))
