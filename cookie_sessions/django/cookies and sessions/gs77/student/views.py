from django.shortcuts import render, HttpResponse

# Create your views here.
def setsession(request):
 request.session['dicts'] = {'name':'Sonam', 'roll':101}
 request.session['lists'] = ['Python', 'Django', 'JavaScript']
 return render(request, 'student/setsession.html')

def getsession(request):
 dicts = request.session['dicts']
 lists = request.session['lists']
 return render(request, 'student/getsession.html', {'dicts':dicts, 'lists':lists})

def delsession(request):
 request.session.flush()
 request.session.clear_expired()
 return render(request, 'student/delsession.html')