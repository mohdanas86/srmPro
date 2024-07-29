from datetime import datetime
from bson import ObjectId
from django.conf import settings
from django.shortcuts import get_object_or_404, render,HttpResponse, redirect
from .models import appraisal_data, appraisal_data_monthwise
from authentication.models import staff, details, src
from .functions import download
from .import logic
from base64 import b64encode


logo = src.objects.get(name='logo')
favicon = src.objects.get(name='favicon icon')
logo_src = logo.image
favicon_src = favicon.image


def s(request):
    return HttpResponse("appraisal working")

def create_apprisal(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        today_date = int(datetime.now().strftime("%d"))
        datesrc = src.objects.get(name="date")
        last_date = int(datesrc.image)
        try:
            data = staff.objects.get(pk=ObjectId(user_id))
            post = appraisal_data.objects.get(Employee_id=data.Employee_id)
            if post:
                    if request.method == 'POST':
                        #Academic Results (CIA, Unit test, End Sem etc.) - Pass %
                        Academic_Score_achived = int(request.POST['Academic_Score_achived'])
                        Academic_achiv = logic.Academic_Score(Academic_Score_achived,post.Academic_Score_cumulative)
                        types = request.POST['Academic_Score_stage']

                        #Online Courses Attended
                        course_achived = int(request.POST['Academic_Score_achived'])
                        course_achiv = logic.online_course(course_achived,post.course_cumulative)
                        c_types = request.POST['course_achived_name']

                        #FDP Attended
                        fdp_week = int(request.POST['fdp_week'])
                        fdp_programs = float(request.POST['fdp_programs'])
                        fdp_achiv = logic.fdp(fdp_week,fdp_programs,post.fdp_cumulative)    

                        #Counselling Students Performance Improvement
                        Counselling_achived = int(request.POST['Counselling_achived'])
                        Counselling_achiv = logic.counselling(Counselling_achived,post.course_cumulative) 

                        #Online Student Feedback                
                        Student_Feedback_achived = int(request.POST['Student_Feedback_achived'])
                        Student_achiv = logic.online_feedback(Student_Feedback_achived,post.Student_Feedback_cumulative)

                        
                        #Perception Improvement : FDP/ Workshop/ Conf. / Branding event / online event / student event organized
                        precption_position = request.POST['precption_achived']
                        precption_achiv = logic.precption(precption_position,post.precption_cumulative)

                        
                        #Research Papers Published in SCI / WoS/ UGC CARE Indexed Journals
                        no_of_Paper = int(request.POST['no_of_Paper'])
                        author_position = request.POST['author_position']
                        research_paper_achive = logic.research_paper(no_of_Paper,int(author_position))

                        #Institutional CoordinatorsIQAC/EXAM Cell/Admissions/MOU
                        Institutional_Coordinators = request.POST['Institutional_Coordinators_achived']
                        if int(Institutional_Coordinators) <=5:
                            Institutional_Coordinators_achived = Institutional_Coordinators
                        else:
                            Institutional_Coordinators_achived = 5

                        #Conference Paper Presentation (Proceedings to be published by reputed publishers like Springer, Elsevier, IEEE etc. & listed in Scopus); Book Chapter/ Book Publication
                        paper_presentaion_type = request.POST['paper_presentaion_type']
                        no_of_paper = int(request.POST.get('no_of_paper'))
                        presentation_achiv = logic.paper_presentaion(no_of_paper,paper_presentaion_type,post.paper_presentaion_cumulative) 

                        #"Research Projects sanctioned - External / Minor(Total amount received in the assessment year)"
                        number_of_project = int(request.POST['no_of_project'])
                        price = int(request.POST['value_of_the_project'])
                        position = request.POST['position']
                        Research_project_sanctioned_achiv = logic.research_project(number_of_project,price,position,post.Research_project_sanctioned_cumulative)  

                        #"Research proposal - PAC Level(PI or CO-PI)"
                        proposal = int(request.POST['proposal'])
                        Research_proposal_achiv = logic.rearsh_proposal(proposal)

                        #Consultancy
                        no_of_project = int(request.POST['No_of_project'])
                        cost = float(request.POST['cost'])
                        Consultancy_achive = logic.consultancy(no_of_project,cost)
                        print(no_of_project, cost, Consultancy_achive)

                        #Use of Innovative Pedagogy with supporting documents (as per NAAC/NBA requirement) 
                        no_of_pedagogy = int(request.POST['no_of_pedagogy'])
                        pedagogy_achive = logic.Pedagogy(no_of_pedagogy)

                        #Design of new curricula and courses/ new experiment / training module
                        number_of_inovative = int(request.POST['number_of_inovative'])
                        inovative_achive = logic.inovative(number_of_inovative)

                        #E-Content development
                        no_Of_content_developement = int(request.POST['no_Of_content_developement'])
                        E_Content_development_achive = logic.content_developement(no_Of_content_developement)

                        #Commitment / Undertaking
                        commitment_undertaking1 = request.POST['i_will1']
                        commitment_undertaking2 = request.POST['i_will2']

                        #additional_information
                        additional_information = request.POST['additional_information']

                        #proof
                        p1 = request.FILES.get('Acadaemic_proof')
                        proof1 = b64encode(p1.read()).decode('utf-8') if p1 else None
                        p2 = request.FILES.get('course_proof')
                        proof2 = b64encode(p2.read()).decode('utf-8') if p2 else None
                        p3 = request.FILES.get('fdp_proof')
                        proof3 = b64encode(p3.read()).decode('utf-8') if p3 else None
                        p4 = request.FILES.get('counselling_proof')
                        proof4 = b64encode(p4.read()).decode('utf-8') if p4 else None
                        p5 = request.FILES.get('Student_feedback_proof')
                        proof5 = b64encode(p5.read()).decode('utf-8') if p5 else None
                        p6 = request.FILES.get('precption_proof')
                        proof6 = b64encode(p6.read()).decode('utf-8') if p6 else None
                        p7 = request.FILES.get('Institutional_coordinators_proof')
                        proof7 = b64encode(p7.read()).decode('utf-8') if p7 else None
                        p8 = request.FILES.get('research_paper_proof')
                        proof8 = b64encode(p8.read()).decode('utf-8') if p8 else None
                        p9 = request.FILES.get('paper_presentaion_proof')
                        proof9 = b64encode(p9.read()).decode('utf-8') if p9 else None
                        p10 = request.FILES.get('Research_project_sanctioned_proof')
                        proof10 = b64encode(p10.read()).decode('utf-8') if p10 else None
                        p11 = request.FILES.get('research_proposal_proof')
                        proof11 = b64encode(p11.read()).decode('utf-8') if p11 else None
                        p12 = request.FILES.get('Consultancy_proof')
                        proof12 = b64encode(p12.read()).decode('utf-8') if p12 else None
                        p13 = request.FILES.get('pedagogy_proof')
                        proof13 = b64encode(p13.read()).decode('utf-8') if p13 else None
                        p14 = request.FILES.get('inovative_proof')
                        proof14 = b64encode(p14.read()).decode('utf-8') if p14 else None
                        p15 = request.FILES.get('E_content_proof')
                        proof15 = b64encode(p15.read()).decode('utf-8') if p15 else None


                        post.Academic_Score_achived = Academic_achiv
                        post.types = types
                        post.course_achived = course_achiv
                        post.c_types = c_types
                        post.fdp_achived = fdp_achiv
                        post.counselling_achived = Counselling_achiv
                        post.Student_Feedback_achived = Student_achiv
                        post.precption_achived = precption_achiv
                        post.Institutional_Coordinators_achived = Institutional_Coordinators_achived
                        post.research_paper_achived = research_paper_achive
                        post.paper_presentaion_achived = presentation_achiv
                        post.Research_project_sanctioned_achived = Research_project_sanctioned_achiv
                        post.Research_proposal_achived = Research_proposal_achiv
                        post.Consultancy_achived = Consultancy_achive
                        post.pedagogy_achived = pedagogy_achive
                        post.inovative_achived = inovative_achive
                        post.E_Content_development_achived = E_Content_development_achive
                        post.Acadaemic_proof=proof1
                        post.course_proof=proof2
                        post.fdp_proof=proof3
                        post.counselling_proof=proof4
                        post.Student_feedback_proof=proof5
                        post.precption_proof=proof6
                        post.Institutional_coordinators_proof=proof7
                        post.research_paper_proof=proof8
                        post.paper_presentaion_proof=proof9
                        post.Research_project_sanctioned_proof=proof10
                        post.research_proposal_proof=proof11
                        post.Consultancy_proof=proof12
                        post.pedagogy_proof=proof13
                        post.inovative_proof=proof14
                        post.E_content_proof=proof15
                        post.save()
                        
                        add = appraisal_data_monthwise(Employee_id = data.Employee_id,
                                 Designation = data.Designation,
                                 Department = data.Department,
                                Academic_Score_cumulative = post.Academic_Score_cumulative, 
                                Academic_Score_achived = Academic_achiv,
                                types = types,
                                course_cumulative = post.course_cumulative, 
                                course_achived = course_achiv,
                                c_types = c_types,
                                fdp_cumulative = post.fdp_cumulative, 
                                fdp_achived = fdp_achiv,
                                counselling_cumulative = post.counselling_cumulative,
                                counselling_achived = Counselling_achiv,
                                Student_Feedback_cumulative = post.Student_Feedback_cumulative,
                                Student_Feedback_achived = Student_achiv,
                                precption_cumulative = post.precption_cumulative, 
                                precption_achived = precption_achiv,
                                Institutional_Coordinators_cumulative = post.Institutional_Coordinators_cumulative,
                                Institutional_Coordinators_achived = Institutional_Coordinators_achived,
                                research_paper_cumulative = post.research_paper_cumulative,     
                                research_paper_achived = research_paper_achive,
                                paper_presentaion_cumulative = post.paper_presentaion_cumulative, 
                                paper_presentaion_achived = presentation_achiv,
                                Research_project_sanctioned_cumulative = post.Research_project_sanctioned_cumulative, 
                                Research_project_sanctioned_achived = Research_project_sanctioned_achiv,
                                Research_proposal_cumulative = post.Research_proposal_cumulative, 
                                Research_proposal_achived = Research_proposal_achiv,
                                Consultancy_cumulative = post.Consultancy_cumulative, 
                                Consultancy_achived = Consultancy_achive,
                                pedagogy_cumulative = post.pedagogy_cumulative, 
                                pedagogy_achived = pedagogy_achive,
                                inovative_cumulative = post.inovative_cumulative, 
                                inovative_achived = inovative_achive,
                                E_Content_development_cumulative = post.E_Content_development_cumulative, 
                                E_Content_development_achived = E_Content_development_achive,
                                Acadaemic_proof = post.Acadaemic_proof,
                                course_proof = post.course_proof,
                                fdp_proof = post.fdp_proof,
                                counselling_proof = post.counselling_proof,
                                Student_feedback_proof = post.Student_feedback_proof,
                                precption_proof = post.precption_proof,
                                Institutional_coordinators_proof = post.Institutional_coordinators_proof,
                                research_paper_proof = post.research_paper_proof,
                                paper_presentaion_proof = post.paper_presentaion_proof,
                                Research_project_sanctioned_proof = post.Research_project_sanctioned_proof,
                                research_proposal_proof = post.research_proposal_proof,
                                Consultancy_proof = post.Consultancy_proof,
                                pedagogy_proof = post.pedagogy_proof,
                                inovative_proof = post.inovative_proof,
                                E_content_proof = post.E_content_proof,
                                commitment_undertaking1 = commitment_undertaking1,
                                commitment_undertaking2 = commitment_undertaking2,
                                additional_information = additional_information)
                        add.save()
                        return redirect('appraisal')
                    return render(request, 'appraisal.html', {"data":post, 'favicon':favicon_src, 'logo':logo_src, 'tdate':today_date, 'ldate':last_date})
            
        except appraisal_data.DoesNotExist:
            add = appraisal_data(Employee_id = data.Employee_id,
                                 Designation = data.Designation,
                                 Department = data.Department,
                                 Academic_Score_cumulative = 0,
                                Academic_Score_achived = 0,
                                Acadaemic_proof = 0,
                                types = 0,
                                course_cumulative = 0,
                                course_achived = 0,
                                course_proof = 0,
                                c_types = 0,
                                fdp_cumulative = 0,
                                fdp_achived = 0,
                                fdp_proof = 0,
                                counselling_cumulative = 0,
                                counselling_achived = 0,
                                counselling_proof = 0,
                                Student_Feedback_cumulative = 0,
                                Student_Feedback_achived = 0,
                                Student_feedback_proof = 0,
                                precption_cumulative = 0,
                                precption_achived = 0,
                                precption_proof = 0,
                                Institutional_Coordinators_cumulative = 0,
                                Institutional_Coordinators_achived = 0,
                                Institutional_coordinators_proof = 0,
                                research_paper_cumulative = 0,
                                research_paper_achived = 0,
                                research_paper_proof = 0,
                                paper_presentaion_cumulative = 0,
                                paper_presentaion_achived = 0,
                                paper_presentaion_proof = 0,
                                Research_project_sanctioned_cumulative = 0,
                                Research_project_sanctioned_achived = 0,
                                Research_project_sanctioned_proof = 0,
                                Research_proposal_cumulative = 0,
                                Research_proposal_achived = 0,
                                research_proposal_proof = 0,
                                Consultancy_cumulative = 0,
                                Consultancy_achived = 0,
                                Consultancy_proof = 0,
                                pedagogy_cumulative = 0,
                                pedagogy_achived = 0,
                                pedagogy_proof = 0,
                                inovative_cumulative = 0,
                                inovative_achived = 0,
                                inovative_proof = 0,
                                E_Content_development_cumulative = 0,
                                E_Content_development_achived = 0,
                                E_content_proof = 0,)
            add.save()
            return redirect('appraisal')
    else:
        return redirect('login')
    
def update_cumulative(request, post_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        data = staff.objects.get(pk=ObjectId(user_id))
        instance = appraisal_data.objects.get(Employee_id=data.Employee_id)
        data_m = get_object_or_404(appraisal_data_monthwise, _id=post_id)
        if instance:

                            # 1 instance.Academic_Score_achived = 0  
                            if instance.Academic_Score_cumulative != 10:
                                if instance.Academic_Score_cumulative + instance.Academic_Score_achived <10:
                                    instance.Academic_Score_cumulative = instance.Academic_Score_cumulative + instance.Academic_Score_achived
                                else:
                                    instance.Academic_Score_cumulative = 10
                            instance.Academic_Score_achived = 0                  

                            # 2 Online Courses Attended
                            if instance.course_cumulative != 5:
                                if instance.course_cumulative + instance.course_achived <= 5:
                                    instance.course_cumulative = instance.course_cumulative + instance.course_achived
                                else:
                                    instance.course_cumulative = 5    
                            instance.course_achived = 0  

                            # 3 FDP Attended
                            if instance.fdp_cumulative != 5:
                                if instance.fdp_cumulative + instance.fdp_achived <= 5:
                                    instance.fdp_cumulative = instance.fdp_cumulative + instance.fdp_achived
                                else:
                                    instance.fdp_cumulative = 5    
                            instance.fdp_achived = 0

                            # 4 Counselling Students Performance Improvement
                            if instance.counselling_cumulative != 3:
                                if instance.counselling_cumulative + instance.counselling_achived <= 3:
                                    instance.counselling_cumulative = instance.counselling_cumulative + instance.counselling_achived
                                else:
                                    instance.counselling_cumulative = 3
                            instance.counselling_achived = 0  

                            # 5 Online Student Feedback 
                            if instance.Student_Feedback_cumulative !=2:
                                if instance.Student_Feedback_cumulative + instance.Student_Feedback_achived <= 2:
                                    instance.Student_Feedback_cumulative = instance.Student_Feedback_cumulative + instance.Student_Feedback_achived
                                else:
                                    instance.Student_Feedback_cumulative = 2
                            instance.Student_Feedback_achived = 0 

                            
                            # 6 Perception Improvement : FDP/ Workshop/ Conf. / Branding event / online event / student event organized     
                            if instance.precption_cumulative != 5:
                                if instance.precption_cumulative + instance.precption_achived <= 5:
                                    instance.precption_cumulative = instance.precption_cumulative + instance.precption_achived
                                else:
                                    instance.precption_cumulative = 5
                            instance.precption_achived = 0  

                            # 7 "Institutional Coordinators IQAC/EXAM Cell/Admissions/MOU"
                            if int(instance.Institutional_Coordinators_cumulative) !=5:
                                if int(instance.Institutional_Coordinators_cumulative) + int(instance.Institutional_Coordinators_achived) <= 5:
                                    instance.Institutional_Coordinators_cumulative = int(instance.Institutional_Coordinators_cumulative) + int(instance.Institutional_Coordinators_achived)
                                    print("add")
                                else:
                                    instance.Institutional_Coordinators_cumulative = 5
                                    print("paste")
                            instance.Institutional_Coordinators_achived = 0        

                            # 8 Research Papers Published in SCI / WoS/ UGC CARE Indexed Journals
                            if instance.research_paper_cumulative < 30:
                                if instance.research_paper_cumulative + instance.research_paper_achived <=30:
                                    instance.research_paper_cumulative = instance.research_paper_cumulative + instance.research_paper_achived
                                else:
                                    instance.research_paper_cumulative = 30
                            instance.research_paper_achived = 0            

                            # 9 Conference Paper Presentation (Proceedings to be published by reputed publishers like Springer, Elsevier, IEEE etc. & listed in Scopus); Book Chapter/ Book Publication
                            if instance.paper_presentaion_cumulative < 8:
                                if instance.paper_presentaion_cumulative + instance.paper_presentaion_achived <= 8:
                                    instance.paper_presentaion_cumulative = instance.paper_presentaion_cumulative + instance.paper_presentaion_achived
                                else:
                                    instance.paper_presentaion_cumulative = 8
                            instance.paper_presentaion_achived = 0 

                            #10 "Research Projects sanctioned - External / Minor(Total amount received in the assessment year)"  
                            if instance.Research_project_sanctioned_cumulative < 10:
                                if instance.Research_project_sanctioned_cumulative + instance.Research_project_sanctioned_achived <= 10:
                                    instance.Research_project_sanctioned_cumulative = instance.Research_project_sanctioned_cumulative + instance.Research_project_sanctioned_achived
                                else:
                                    instance.Research_project_sanctioned_cumulative = 10
                            instance.Research_project_sanctioned_achived = 0  

                            #11 "Research proposal - PAC Level(PI or CO-PI)"
                            if instance.Research_proposal_cumulative < 3:
                                if instance.Research_proposal_cumulative + instance.Research_proposal_achived <= 3:
                                    instance.Research_proposal_cumulative = instance.Research_proposal_cumulative + instance.Research_proposal_achived
                                else:
                                    instance.Research_proposal_cumulative = 3
                            instance.Research_proposal_achived = 0    

                            #12 Consultancy
                            if instance.Consultancy_cumulative < 3:
                                if instance.Consultancy_cumulative + instance.Consultancy_achived <= 3:
                                    instance.Consultancy_cumulative =  instance.Consultancy_cumulative + instance.Consultancy_achived
                                else:
                                    instance.Consultancy_cumulative = 3
                            instance.Consultancy_achived = 0  
                            
                            #13 Use of Innovative Pedagogy with supporting documents (as per NAAC/NBA requirement) 
                            if instance.pedagogy_cumulative < 6:
                                if instance.pedagogy_cumulative + instance.pedagogy_achived <= 6:
                                    instance.pedagogy_cumulative = instance.pedagogy_cumulative + instance.pedagogy_achived
                                else:
                                    instance.pedagogy_cumulative = 6
                            instance.pedagogy_achived = 0    

                            #14 Design of new curricula and courses/ new experiment / training module
                            if instance.inovative_cumulative < 2.5:
                                if instance.inovative_cumulative + instance.inovative_achived <= 2.5:
                                    instance.inovative_cumulative = instance.inovative_cumulative + instance.inovative_achived
                                else:
                                    instance.inovative_cumulative = 2.5
                            instance.inovative_achived = 0  

                            #15 E-Content development
                            if instance.E_Content_development_cumulative < 2.5:
                                if instance.E_Content_development_cumulative + instance.E_Content_development_achived <= 2.5:
                                    instance.E_Content_development_cumulative = instance.E_Content_development_cumulative + instance.E_Content_development_achived 
                                else:
                                    instance.E_Content_development_cumulative = 2.5
                            instance.E_Content_development_achived = 0         

                            instance.save()

                            data_m.chairman_approved = True
                            data_m.chairman_approved_date = datetime.now()
                            data_m.save()

                            return redirect('show_apprisal')

def show_apprisal(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        data = staff.objects.get(pk=ObjectId(user_id))
        ap_data = appraisal_data_monthwise.objects.filter(Employee_id = data.Employee_id)
        return render(request, 'apprisal_data.html', {'ap_data': ap_data, 'data': data,'favicon':favicon_src, 'logo':logo_src})
    else:
        return redirect('login')
    
def download_pdf(request, post_id):
    if 'user_id' in request.session:
        post = get_object_or_404(appraisal_data_monthwise, _id=post_id)
        n = get_object_or_404(staff, Employee_id=post.Employee_id)
        h = get_object_or_404(staff, Department=post.Department, Designation="HOD")
        d = get_object_or_404(staff, Designation="DEAN")
        data = [
                    ['SI.NO','FUNCTIONAL AREAS', 'Cumulative', 'Achived'],
                    ["1",f"Academic Results (CIA, Unit test, End Sem etc.) - Pass %- {post.types}", post.Academic_Score_cumulative, post.Academic_Score_achived],
                    ["2",f"Online Courses Attended - {post.c_types}", post.course_cumulative, post.course_achived],
                    ["3","FDP Attended", post.fdp_cumulative, post.fdp_achived],
                    ["4","Counselling Students Performance Improvement", post.counselling_cumulative, post.counselling_achived],
                    ["5","Online Student Feedback", post.Student_Feedback_cumulative, post.Student_Feedback_achived],
                    ["6","Perception Improvement : FDP/ \n Workshop/ Conf. / Branding event / \n online event / student event organized", post.precption_cumulative, post.precption_achived],
                    ["7","Institutional Coordinators\n IQAC/EXAM Cell/Admissions/MOU",post.Institutional_Coordinators_cumulative, post.Institutional_Coordinators_achived],]
        
        data1 =[['SI.NO','FUNCTIONAL AREAS', 'Cumulative', 'Achived'],
                ["8","Research Papers Published in SCI / WoS/ UGC CARE\n Indexed Journals", post.research_paper_cumulative, post.research_paper_achived],
                ["9","Conference Paper Presentation \n(Proceedings to be published by reputed\n publishers like Springer, Elsevier, IEEE\n etc. & listed in Scopus); Book Chapter/\n Book Publication", post.paper_presentaion_cumulative, post.paper_presentaion_achived],]
        
        data2 =[['SI.NO','FUNCTIONAL AREAS', 'Cumulative', 'Achived'],
                ["10","Research Projects sanctioned - External / Minor (Total amount \nreceived in the\n assessment year)", post.Research_project_sanctioned_cumulative, post.Research_project_sanctioned_achived],
                ["11","Research proposal - PAC Level(PI or CO-PI)", post.Research_proposal_cumulative, post.Research_proposal_achived],
                ["12","Consultancy", post.Consultancy_cumulative, post.Consultancy_achived],]
        
        data3 = [['SI.NO','FUNCTIONAL AREAS', 'Cumulative', 'Achived'],
                ["13","Use of Innovative Pedagogy with supporting documents (as per \nNAAC/NBA requirement) ", post.pedagogy_cumulative, post.pedagogy_achived],
                ["14","Design of new curricula and courses/\n new experiment / training module", post.inovative_cumulative, post.inovative_achived],
                ["15","E-Content development", post.E_Content_development_cumulative, post.E_Content_development_achived],
                ]
        
        p_data = [
            [f"NAME OF THE FACULTY: {n.name}","      ","      ",f"DESIGNATION : {post.Designation}"],
            [f"DEPARTMENT NAME: {post.Department}","      ","      ",f"REPORTING PERIOD: {post.date}"]
        ]

        data4 = [['SI.NO','FUNCTIONAL AREAS', 'Achived score'],
            ["1", "Academic Marks", post.Academic_Score_achived + post.course_achived + post.counselling_achived + post.fdp_achived + post.Student_Feedback_achived + post.precption_achived + int(post.Institutional_Coordinators_achived)],
            ["2", "Resaerch Marks", post.research_paper_achived + post.paper_presentaion_achived],
            ["3", "Co-curricular & Extension", post.pedagogy_achived + post.inovative_achived + post.E_Content_development_achived],
        ]

        p_data1 = [
            [f"Date: {post.date}","            ","           ",f"{n.name}"],
            [f"                          ","      ","        ",f"E-Signature of the Faculty Member"]
        ]

        if post.hod_approved == True:
            p_data2 = [
                [f"Date: {post.hod_approved_date}","            ","      ",f"{h.name}"],
                [f"                          ","      ","                ",f"E-Signature of HOD"]
            ]
        else:
            p_data2 = [
                [f"Date:                        ","      ","      ","          "],
                [f"                          ","      ","         ",f"E-Signature of HOD"]
            ]

        if post.dean_approved == True:
            p_data3 = [
                [f"Date: {post.dean_approved_date}","            ","      ",f"{d.name}"],
                [f"                          ","      ","                 ",f"E-Signature of HOI"]
            ]
        else:
            p_data3 = [
                [f"Date:                        ","      ","            ","          "],
                [f"                          ","      ","                ",f"E-Signature of the HOI"]
            ]

        if post.chairman_approved == True:
            p_data4 = [
                [f"Date: {post.chairman_approved_date}","            ","      ",f"{n.name}"],
                [f"                          ","      ","                ",f"E-Signature of HOD"]
            ]
        else:
            p_data4 = [
                [f"Date:                        ","      ","      ","          "],
                [f"                          ","      ","         ",f"E-Signature of HOD"]
            ]

        try:
            pdf_response = download(data, data1, data2, data3, p_data, data4, p_data1, p_data2, p_data3, p_data4, 
                                    post.commitment_undertaking1, post.commitment_undertaking2, 
                                    post.additional_information, logo_src)
            return pdf_response
        except Exception as e:
                return HttpResponse(f"Error generating in generate pdf: {str(e)}")           
    else:
        return redirect('login') 


def edit_apprisal(request, post_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        data = staff.objects.get(pk=ObjectId(user_id))
        ap_data = appraisal_data_monthwise.objects.get(pk=ObjectId(post_id))

        if not ap_data.query:
            return redirect('show_apprisal')
        
        if request.method == 'POST':
            print(f"Current ap_data.query value: {ap_data.query}")
            ap_data.query = False
            ap_data.save()
            print(f"Current ap_data.query value: {ap_data.query}")
            return redirect('show_apprisal')
        return render(request, 'edit.html', {'ap_data': ap_data, 'data': data,'favicon':favicon_src, 'logo':logo_src})
    else:
        return redirect('login')