import base64
from bson import ObjectId
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from appraisal.models import appraisal_data, appraisal_data_monthwise
from authentication.models import staff, src
from .import functions
from datetime import datetime

logo = src.objects.get(name='logo')
favicon = src.objects.get(name='favicon icon')
logo_src = logo.image
favicon_src = favicon.image

def data(request, post_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        check = get_object_or_404(staff, _id=ObjectId(user_id))
        data_m = get_object_or_404(appraisal_data_monthwise, _id=post_id)
        data = get_object_or_404(appraisal_data, Employee_id=data_m.Employee_id)
        n = get_object_or_404(staff, Employee_id=data.Employee_id)

        if check.Designation == "HOD":
            am = data_m.Academic_Score_achived + data_m.course_achived + data_m.counselling_achived + data_m.fdp_achived + data_m.Student_Feedback_achived + data_m.precption_achived + int(data_m.Institutional_Coordinators_achived)
            rm = data_m.research_paper_achived + data_m.paper_presentaion_achived
            cm = data_m.pedagogy_achived + data_m.inovative_achived + data_m.E_Content_development_achived
            
            if 'approve_button' in request.POST:
                data_m.hod_approved = True
                data_m.hod_approved_date = datetime.now()
                data_m.save()
                return redirect('approved')
            
            if 'query_button' in request.POST:
                query = request.POST['query_box']
                t = "\n Thanking you"
                message = "Respected Faculty,\n \t" + query + t.center(100)
                functions.sent(n.email, message)
                data_m.query = True
                data_m.save()
                msg = "Query sent successfully"
                return render(request, 'approvel_check.html', {"data": data_m, 'msg': msg, 'name': n.name, "am": am, "rm": rm, "cm": cm, 'favicon': favicon_src, 'logo': logo_src})
            
            return render(request, 'approvel_check.html', {"data": data_m, 'name': n.name, "am": am, "rm": rm, "cm": cm, 'favicon': favicon_src, 'logo': logo_src})
        else:
            return HttpResponse("You don't have access to this page.")
    else:
        return redirect('login')

def d_data(request, post_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        check = get_object_or_404(staff, _id=ObjectId(user_id))
        data_m = get_object_or_404(appraisal_data_monthwise, _id=post_id)
        data = get_object_or_404(appraisal_data, Employee_id=data_m.Employee_id)
        n = get_object_or_404(staff, Employee_id=data.Employee_id)

        if check.Designation == "DEAN":
            am = data_m.Academic_Score_achived + data_m.course_achived + data_m.counselling_achived + data_m.fdp_achived + data_m.Student_Feedback_achived + data_m.precption_achived + int(data_m.Institutional_Coordinators_achived)
            rm = data_m.research_paper_achived + data_m.paper_presentaion_achived
            cm = data_m.pedagogy_achived + data_m.inovative_achived + data_m.E_Content_development_achived
            
            if 'approve_button' in request.POST:
                data_m.dean_approved = True
                data_m.dean_approved_date = datetime.now()
                data_m.save()
                return redirect('check')
            
            return render(request, 'd_approvel_check.html', {"data": data_m, 'name': n.name, "am": am, "rm": rm, "cm": cm, 'favicon': favicon_src, 'logo': logo_src})
        else:
            return HttpResponse("You don't have access to this page.",status=403)
    else:
        return redirect('login')
 
    
def c_approve(request, post_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        check = get_object_or_404(staff, _id=ObjectId(user_id))
        if check.Designation == 'DEAN':
            data_m = get_object_or_404(appraisal_data_monthwise, _id=post_id)
            data_m.dean_approved = True
            data_m.chairman_approved_date = datetime.now()
            data_m.save()
            return redirect('check')
        else:
            return HttpResponse("Unauthorized", status=403)
    else:
        return redirect('login')   