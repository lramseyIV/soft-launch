from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead, AdminUser
import bcrypt
import djqscsv
# Create your views here.
def index (request):
    return render (request, "index.html")

def sign_up(request): # display page for sign up form
    return render (request, "sign_up.html")

def submit_lead(request): # handles saving the info from user
    if request.method=="POST":
        # make sure that email is unique
        if Lead.objects.filter(email=request.POST['email']):
            messages.error (request, "Email already submitted.")
            return redirect('/sign_up')
        Lead.objects.create(name=request.POST['fname'], title=request.POST['title'], email=request.POST['email'])
        return redirect ('/thankyou')

def thanks(request):
    return render (request, "thankyou.html")

def adminLogin(request):
    if request.method=="GET":
        return render (request, "admin-login.html")
    if request.method=="POST":
        if AdminUser.objects.filter(username=request.POST['username']):
            admin = AdminUser.objects.get(username=request.POST['username'])
            if bcrypt.checkpw(request.POST['password'].encode(), admin.password.encode()):
                request.session['id'] = admin.id
                return redirect('/dashboard')
            else:
                return redirect('/')
        else:
            return redirect('/')

def dashboard(request):
    if 'id' in request.session:
        if AdminUser.objects.filter(id=request.session['id']):
            context = {
                "leads": Lead.objects.all(),
                "num_interested": len(Lead.objects.all())
            }
            return render (request, "dashboard.html", context)
        else:
            return redirect ('/')
    else:
        return redirect ('/')

def delete_lead(request, uid):
    if 'id' in request.session:
        if AdminUser.objects.filter(id=request.session['id']):
            lead = Lead.objects.get(id=uid)
            lead.delete()
            return redirect('/dashboard')
        else:
            return redirect('/')
    else:
        return redirect('/')

def get_csv(request):
    if 'id' in request.session:
        if AdminUser.objects.filter(id=request.session['id']):
            qs = Lead.objects.all()
            return djqscsv.render_to_csv_response(qs)
        else:
            return redirect('/')
    else:
        return redirect('/')