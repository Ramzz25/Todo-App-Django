from django.shortcuts import render
from todo_app.forms import UserForm, todoForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from todo_app.models import todo_item,User
# Create your views here.

def index(request):

    return render(request, 'todo_app/index.html')

def register(request):

    registered = False
    
    if request.method=="POST":

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            return HttpResponse("Invalid details")

    else:
        user_form = UserForm()

    return render(request,'todo_app/registration.html',{
                            'registered':registered,
                            'user_form':user_form})

def user_login(request):

    if( request.method=="POST" ):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if( user ):
            if(user.is_active):
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                

            else:
                return HttpResponse("Account Not Active")
        else:
            print('Someone tried to login and failed!!')
            print("Username : {} and Password : {}".format(username,password))
            return HttpResponse("Invalid credentials")

    else:
        return render(request,'todo_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def add_note(request):

    if request.method=="POST":
        todo_form = todoForm(data=request.POST)

        if todo_form.is_valid():
            todo_item.objects.create(user=request.user, title=request.POST.get('title'), description=request.POST.get('description'))
        else:
            return HttpResponse("Invalid details")
        
        
    todo_form = todoForm()
    return render(request,'todo_app/add_note.html',{'todo_form':todo_form})

@login_required
def view_note(request):
    currentUser_id = request.user.id
    usr = User.objects.get(pk=currentUser_id)
    objs = todo_item.objects.filter(user=usr)
    list_isThere = True
    
    if(len(objs)==0):
        list_isThere=False
        objs = {}
        heading = "Hey, There!"
        message = "You have nothing in your notes. Go To \'Add a note\' to add notes"
        objs[heading] = message

    return render(request,'todo_app/view_note.html',{'todo_list':objs,'list_isThere':list_isThere})

@login_required
def delete_item(request, todo_id):

    itm_to_delete = todo_item.objects.get(id=todo_id)
    itm_to_delete.delete()
    return HttpResponseRedirect(reverse('todo_app:view_note'))

