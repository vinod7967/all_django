from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setcookie(request):

 response = render(request, 'student/setcookie.html')
 #response.set_cookie('name','sonam')
 #response.set_cookie('name','sonam',max_age=120)
 response.set_cookie('lname', 'Jha', expires=datetime.utcnow()+timedelta(days=2))
 return response

def getcookie(request):
  name = request.COOKIES['name']
 # name = request.COOKIES.get('name')
# name = request.COOKIES.get('name', "Guest")
  return render(request, 'student/getcookie.html', {'name':name})

def delcookie(request):
 reponse = render(request, 'student/delcookie.html')
 reponse.delete_cookie('name')
 return reponse