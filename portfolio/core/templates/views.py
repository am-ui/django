#from core.models import Post
from django.shortcuts import render

# Create your views here.
def home(request):
  context = {'home': 'active'}
  return render(request, 'core/home.html', context)

def contact(request):
  context = {'contact': 'active'}
  return render(request, 'core/contact.html', context)

"""

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Email'):
            post=Post()
            post.Name= request.POST.get('Name')
            post.Email= request.POST.get('Email')
            post.Subject= request.POST.get('Subject')
            post.Message= request.POST.get('Message')
            post.save()
            return render(request, 'core/contact.html')  

        else:
            return render(request,'core/contact.html')

"""