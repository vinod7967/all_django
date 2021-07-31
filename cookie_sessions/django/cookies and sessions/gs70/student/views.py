from django.shortcuts import render

# Create your views here.
def setsession(request):
 request.session['name'] = 'fariha'
 request.session['lname'] = 'john'
 return render(request, 'student/setsession.html')

def getsession(request):
 # name = request.session['name']
 name = request.session.get('name')
 lname = request.session.get('lname')
 return render(request, 'student/getsession.html', {'name':name, 'lname':lname})

def delsession(request):
 if 'name' in request.session:
  del request.session['name']
 return render(request, 'student/delsession.html')