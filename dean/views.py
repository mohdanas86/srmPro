from bson import ObjectId
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from appraisal.models import appraisal_data_monthwise
from authentication.models import staff, details, src

logo = src.objects.get(name='logo')
favicon = src.objects.get(name='favicon icon')
logo_src = logo.image
favicon_src = favicon.image

def dean(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'DEAN':
            return render(request, 'd_home.html', {'favicon':favicon_src, 'logo':logo_src })
        else:
            return HttpResponse("Unauthorized", status=403)
    else:
        return redirect('login')

def department(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'DEAN':
            try:
                distinct_departments = details.objects.values('Department').distinct()
                return render(request, 'dep.html', {'distinct_departments': distinct_departments, 'favicon': favicon_src, 'logo': logo_src })
            except staff.DoesNotExist:
                pass
        else:
            return HttpResponse("Unauthorized", status=403)
    return redirect('login')

def show_staff(request, department):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'DEAN':
            try:
                data = details.objects.filter(Department=department)
                if request.method == 'POST':        
                        employee_id = request.POST.get('nameInput')
                        name = request.POST.get('positionInput')
                        department = request.POST.get('departmentInput')
                        designation = request.POST.get('DesignationInput')
                        email = request.POST.get('emailInput')
                        password = employee_id + "123"
                        new_staff = staff(Employee_id=employee_id, name=name, password=make_password(password), email=email, Department=department, Designation=designation)
                        new_staff.save()
                        return redirect('show_staff', department=department)
                return render(request, 'show_s.html', {'data': data,'dep':department, 'favicon': favicon_src, 'logo': logo_src })
            except staff.DoesNotExist:
                pass
        else:
            return HttpResponse("Unauthorized", status=403)    
    return redirect('login') 

def add_staff_d(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        hod = staff.objects.filter(Designation="HOD")        
        if staff_d.Designation == 'DEAN':
            if request.method == 'POST':        
                employee_id = request.POST.get('nameInput')
                name = request.POST.get('positionInput')
                department = request.POST.get('departmentInput')
                designation = request.POST.get('DesignationInput')
                email = request.POST.get('emailInput')
                password = employee_id + "123"
                new_staff = staff(Employee_id=employee_id, name=name, password=make_password(password), email=email, Department=department, Designation=designation)
                new_staff.save()
                return redirect('staff_d')
            return render(request, 'add.html', {'data': hod,'favicon': favicon_src, 'logo': logo_src })
        else:
            return HttpResponse("Unauthorized", status=403)    
    return redirect('login') 


def d_approval(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'DEAN':
            distinct_departments = details.objects.values('Department').distinct()
            data = appraisal_data_monthwise.objects.all()
            return render(request, 'd_approve.html', {'data':data, 'distinct_departments':distinct_departments,'favicon':favicon_src, 'logo':logo_src })
        else:
            return HttpResponse("Unauthorized", status=403)
    else:
        return redirect('login')
    
def d_approved(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'DEAN':
            distinct_departments = details.objects.values('Department').distinct()
            data = appraisal_data_monthwise.objects.all()
            return render(request, 'd_approved.html', {'data':data, 'distinct_departments':distinct_departments,'favicon':favicon_src, 'logo':logo_src })
        else:
            return HttpResponse("Unauthorized", status=403)
    else:
        return redirect('login')
