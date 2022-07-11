
from django.http import HttpResponse
from django.shortcuts import render,redirect


from .models import *

# Create your views here.
def Indexpage(request):
    return render(request,"app/index.html")

def Signuppage(request):
    return render(request,"app/signup.html")

def Register(request):
    if request.method=="POST":
    
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        Contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already exist"

            return render(request,"app/signup.html", {'msg':message})

        else:
            if password == cpassword:
                newuser = UserMaster.objects.create(email=email,password=password)
                newcand = User.objects.create(user_id=newuser,firstname=fname,lastname=lname,contact=Contact)

                return render(request,"app/login.html")
            else:
                message = "Password mismatch"
                return render(request,"app/signup.html", {'msg':message})

def Loginpage(request):
    return render(request,"app/login.html")

def LoginUser(request):

        email = request.POST['email']
        password = request.POST['password']


        user = UserMaster.objects.get(email=email)

        if user:
            if user.password==password:
                can = User.objects.get(user_id=user)
                request.session['id'] = user.id
                
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['contact'] = can.contact
                request.session['email'] = user.email
                request.session['password'] = user.password

                return render(request,"app/home.html")
            else:
                message = "Incorrect Password!!"
                return render(request,"app/login.html",{'msg':message})

        else:
            message = "User does not exists"
            return render(request,"app/login.html",{'msg':message})


def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = User.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user, 'can':can})

def Homepage(request):
    return render(request,"app/home.html")

def Createpage(request):
    return render(request,"app/create.html")


def Create(request,pk):
    user = UserMaster.objects.get(pk=pk)
    
    if request.method == "POST":
        
        can = User.objects.get(user_id=user)
        can.question = request.POST['question']
        
        question = request.POST['question']
        option1 = request.POST['op1']
        option2 = request.POST['op2']
        option3 = request.POST['op3']
        option4 = request.POST['op4']
        
        newquestion = Poll.objects.create(user_id=can,question=question,option1=option1,option2=option2,option3=option3,option4=option4)
        
        
        
        

        message = "Poll created successfully!"
        return render(request,"app/create.html",{'msg':message})

    else:
        message = "Invalid action!!"
        return redirect('createpage')
    

def POllpage(request):
    all_poll = Poll.objects.all()
    return render(request,"app/vote.html",{'all_poll':all_poll})

def Vote(request,pk):
    poll = Poll.objects.get(pk=pk)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'app/vote.html', context)


def results(request, pk):
    poll = Poll.objects.get(pk=pk)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)

def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')