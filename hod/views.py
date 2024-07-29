from bson import ObjectId
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from authentication.models import staff, details, src
from appraisal.models import appraisal_data, appraisal_data_monthwise
from home.models import detail

logo = src.objects.get(name='logo')
favicon = src.objects.get(name='favicon icon')
logo_src = logo.image
favicon_src = favicon.image

def head(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'HOD':
            return render(request, 'h_home.html', {'favicon':favicon_src, 'logo':logo_src })
        else:
            return HttpResponse("Unauthorized", status=403)
    else:
        return redirect('login')
    
def approval(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'HOD':
            data = appraisal_data_monthwise.objects.filter(Department="MCA")
            return render(request, 'approve.html', {'data':data,'favicon':favicon_src, 'logo':logo_src })
        else:
            return HttpResponse("Unauthorized", status=403)
    else:
        return redirect('login')
    
def approved(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'HOD':
            data = appraisal_data_monthwise.objects.filter(Department="MCA")
            return render(request, 'approved.html', {'data':data,'favicon':favicon_src, 'logo':logo_src })
        else:
            return HttpResponse("Unauthorized", status=403)
    else:
        return redirect('login')   

def staff_data(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'HOD':
            try:
                dep = staff.objects.get(_id=ObjectId(user_id))
                data = details.objects.filter(Department=dep.Department)
                if request.method == 'POST':        
                    employee_id = request.POST.get('nameInput')
                    name = request.POST.get('positionInput')
                    department = request.POST.get('departmentInput')
                    designation = request.POST.get('DesignationInput')
                    email = request.POST.get('emailInput')
                    password = employee_id + "123"
                    new_staff = staff(Employee_id=employee_id, name=name, password=make_password(password), email=email, Department=department, Designation=designation)
                    new_staff.save()
                    return redirect('staff')
                return render(request, 'staff.html', {'data': data,'dep':dep.Department, 'favicon': favicon_src, 'logo': logo_src })
            except staff.DoesNotExist:
                pass
        else:
            return HttpResponse("Unauthorized", status=403)    
    return redirect('login')   

def staff_delete(request, employee_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'HOD' or staff_d.Designation == 'DEAN':
            staffsl = get_object_or_404(staff, Employee_id=employee_id)
            # staffsd = get_object_or_404(details, Employee_id=employee_id)
            staffsl.delete()
            # staffsd.delete()
            if staff_d.Designation == 'HOD':
                return redirect("staff")
            elif staffsl.Designation == 'HOD':
                return redirect('staff_d')
            else:
                return redirect("departments")
        else:
            return HttpResponse("Unauthorized", status=403)    
    return redirect('login')   

def view_staff(request, employee_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']        
        staff_d = staff.objects.get(_id=ObjectId(user_id))
        if staff_d.Designation == 'HOD' or staff_d.Designation == 'DEAN':
            try:
                deta = detail.objects.get(employee_id=employee_id)
                return render(request, 'view_staff.html', {
                    'data':deta,
                    'favicon': favicon_src,
                    'logo': logo_src
                    })
            except detail.DoesNotExist:
                return HttpResponse("Staff has not filled the profile", status=403)
        else:
            return HttpResponse("Unauthorized", status=403)    
    return redirect('login')   



