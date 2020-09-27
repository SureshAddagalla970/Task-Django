from django.shortcuts import render, HttpResponseRedirect
from .forms import EmployeeReg
from .models import User

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm = EmployeeReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            coun = fm.cleaned_data['country']
            sta = fm.cleaned_data['state']
            pin = fm.cleaned_data['pincode']
            reg = User(name=nm, email=em, address=ad,
                       country=coun, state=sta, pincode=pin)

            reg.save()
            fm = EmployeeReg()
    else:
        fm = EmployeeReg()

    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EmployeeReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = EmployeeReg(instance=pi)

    return render(request, 'enroll/update.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
