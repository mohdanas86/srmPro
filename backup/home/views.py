from base64 import b64encode
from bson import ObjectId
from django.shortcuts import render,redirect, HttpResponse
from authentication.models import staff, details, src
from .models import detail

logo = src.objects.get(name='logo')
favicon = src.objects.get(name='favicon icon')
logo_src = logo.image
favicon_src = favicon.image

def home(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        try:
            data = staff.objects.get(pk=ObjectId(user_id))
            try:
                deta = detail.objects.get(employee_id=data.Employee_id)
                return render(request, 'home.html', {
                    'data':deta,
                    'favicon': favicon_src,
                    'logo': logo_src
                })
            except detail.DoesNotExist:
                if request.method == 'POST':
                    campus = request.POST.get('campus')
                    college_name = request.POST.get('college_name')
                    email_address = request.POST.get('Email_Address')
                    employee_id = request.POST.get('Employee_id')
                    department = request.POST.get('Department')
                    name_of_faculty = request.POST.get('Name_of_the_faculty')
                    gender = request.POST.get('Gender')
                    date_of_birth = request.POST.get('Date_of_Birth')
                    designation = request.POST.get('Designation')
                    year_of_joining = request.POST.get('Year_of_joining')
                    srm_experience = request.POST.get('SRM_experience_Year')
                    other_college_experience = request.POST.get('Other_college_experience_Year')
                    industry_experience = request.POST.get('industry_experience')
                    image = request.FILES.get('image_file')
                    Passport_size_photo = b64encode(image.read()).decode("utf-8")

                    ug = request.POST.get('ug')
                    ug_university = request.POST.get('Name_of_the_Universityug')
                    ug_place = request.POST.get('ug_place')
                    ug_percentage = request.POST.get('ug_percentage')
                    ug_mode = request.POST.get('ugmode')
                    if ug_mode == 'Part-time':
                        ug_parttime_mode = request.POST.get('parttime_modeug')
                    else:
                        ug_parttime_mode = ""

                    ug_period = request.POST.get('ug_period')
                    ug_class = request.POST.get('ugclass')
                    if ug_class == '1st Class with Distinction':
                        ug_ur = request.POST.get('ug_university_rank')
                        ug_cr = request.POST.get('ug_college_rank')
                    else:
                        ug_ur = ""
                        ug_cr = ""
                    
                    pg = request.POST.get('pg')
                    pg_university = request.POST.get('Name_of_the_Universitypg')
                    pg_place = request.POST.get('ug_place')
                    pg_percentage = request.POST.get('pg_percentage')
                    pg_mode = request.POST.get('pgmode')
                    if pg_mode == 'Part-time':
                        pg_parttime_mode = request.POST.get('parttime_modepg')
                    else:
                        pg_parttime_mode = ""
                    
                    pg_period = request.POST.get('pg_period')
                    pg_class = request.POST.get('pgclass')
                    if pg_class == '1st Class with Distinction':
                        pg_ur = request.POST.get('pg_university_rank')
                        pg_cr = request.POST.get('pg_college_rank')
                    else:
                        pg_ur = ""
                        pg_cr = ""

                    phd = request.POST.get('phd')
                    phd_university = request.POST.get('Name_of_the_Universityphd')
                    phd_place = request.POST.get('phd_place')
                    phd_duration = request.POST.get('phd_Duration')
                    phd_percentage = request.POST.get('phd_percentage')
                    year_of_completion = request.POST.get('Year_of_completion')
                    phd_mode = request.POST.get('phdmode')
                    if phd_mode == "Full-time":
                        phd_fulltime_mode = request.POST.get('fulltime_modephd')
                    else:
                        phd_fulltime_mode = ""

                    diploma = request.POST.get('Diploma')

                    name_of_course = request.POST.get('name_of_the_cource')
                    university_for_course = request.POST.get('Name_of_the_college')
                    diploma_percentage = request.POST.get('diploma_Percentage')
                    diploma_class = request.POST.get('dclass')

                    research_area = request.POST.get('Research_Area')
                    total_indexed_papers = request.POST.get('Total_No_of_papers_published')
                    ugc_care_papers = request.POST.get('No_of_Papers_Published_in_UGC_Care_Journal')
                    scopus_papers = request.POST.get('No_of_Papers_Published_in_Scopus_Indexed_Journal')
                    web_of_science_papers = request.POST.get('No_of_Papers_Published_in_Web_of_Science_Journal')
                    sci = request.POST.get('SCI')
                    national_conf_presented = request.POST.get('No_of_National_Conference_Presented')
                    conference_proceedings_isbn = request.POST.get('No_of_papers_published_in_conference_proceedings_with_ISBN_number')

                    Patentp = request.POST.get('Patent')
                    number_p = request.POST.get('number')
                    if Patentp == "yes":
                        num_p = int(number_p)
                        patent = {}
                        for i in range(1, num_p + 1):
                            label = f'Patent {i}'
                            Patent_name = request.POST.get(f'patent_name{i}')
                            Patent_investieater = request.POST.get(f'investieater{i}')
                            # Patent_commercialized = request.POST.get(f'Patent_commercialized{i}')
                            Patent_status = request.POST.get(f'Patent_status{i}')
                            patent[label] = {
                                f'Patent_name{i}': Patent_name,
                                f'Patent_investieater{i}': Patent_investieater,
                                # f'Patent_commercialized{i}': Patent_commercialized,
                                f'Patent_status{i}': Patent_status
                            }
                    else:
                        patent = {}
                    
                    bookb = request.POST.get('Books')
                    number_b = request.POST.get('number_b')
                    if bookb == "yes":
                        num_b = int(number_b)
                        book = {}
                        for i in range(1, num_b + 1):
                            label = f'Book {i}'
                            Book_Title = request.POST.get(f'Book_Title{i}')
                            Book_publisher_name = request.POST.get(f'Book_publisher_name{i}')
                            isbn_number = request.POST.get(f'isbn_number{i}')
                            Year_of_publication = request.POST.get(f'Year_of_publication{i}')
                            Chapters = request.POST.get(f'Chapters{i}')
                            book[label] = {
                                f'Book_Title{i}': Book_Title, 
                                f'Book_publisher_name{i}': Book_publisher_name,
                                f'isbn_number{i}': isbn_number, 
                                f'Year_of_publication{i}': Year_of_publication,
                                f'Chapters{i}': Chapters
                            }
                    else:
                        book = {}
                    
                    fdpa = request.POST.get('fdp_attended')
                    number_f = request.POST.get('number_f')
                    if fdpa == "yes":
                        num_f = int(number_f)
                        fdp = {}
                        for i in range(1, num_f + 1):
                            label = f'FDP {i}'
                            Name_of_the_fdp = request.POST.get(f'Name_of_the_fdp{i}')
                            Duration = request.POST.get(f'Duration{i}')
                            Organized_by = request.POST.get(f'Organized_by{i}')
                            Sponsored_by = request.POST.get(f'Sponsored_by{i}')
                            mode = request.POST.get(f'mode{i}')
                            fdp[label] = {
                                f'Name_of_the_fdp{i}': Name_of_the_fdp, 
                                f'Duration{i}': Duration, 
                                f'Organized_by{i}': Organized_by,
                                f'Sponsored_by{i}': Sponsored_by,
                                f'mode{i}': mode
                            }
                    else:
                        fdp = {}

                    workshopa = request.POST.get('workshop_attended')
                    number_w = request.POST.get('number_w')
                    if workshopa == "yes":
                        num_w = int(number_w)
                        workshop = {}
                        for i in range(1, num_w + 1):
                            label = f'workshop {i}'
                            Name_of_the_workshop = request.POST.get(f'Name_of_the_workshop{i}')
                            Duration = request.POST.get(f'Duration{i}')
                            Organized_by = request.POST.get(f'Organized_by{i}')
                            Sponsored_by = request.POST.get(f'Sponsored_by{i}')
                            mode = request.POST.get(f'mode{i}')
                            workshop[label] = {
                                f'Name_of_the_workshop{i}': Name_of_the_workshop, 
                                f'Duration{i}': Duration, 
                                f'Organized_by{i}': Organized_by,
                                f'Sponsored_by{i}': Sponsored_by,
                                f'mode{i}': mode
                            }
                    else:
                        workshop = {}

                    Projectsa = request.POST.get('projects_detials')
                    number_pr = request.POST.get('number_pr')
                    if Projectsa == "yes":
                        num_pr = int(number_pr)
                        Projects = {}
                        for i in range(1, num_pr + 1):
                            label = f'Projects {i}'
                            Title_of_project = request.POST.get(f'Title_of_project{i}')
                            Applied_to = request.POST.get(f'Applied_to{i}')
                            Applied_Date = request.POST.get(f'Applied_Date{i}')
                            Projects[label] = {
                                f'Title_of_project{i}': Title_of_project, 
                                f'Applied_to{i}': Applied_to, 
                                f'Applied_Date{i}': Applied_Date
                            }
                    else:
                        Projects = {}

                    Projectss = request.POST.get('projects_sanctioned_detials')
                    number_prs = request.POST.get('number_prs')
                    if Projectss == "yes":
                        num_prs = int(number_prs)
                        projects_sanctioned_detials = {}
                        for i in range(1, num_prs + 1):
                            label = f'projects_sanctioned_detials {i}'
                            Title_of_projects = request.POST.get(f'Title_of_projects{i}')
                            Sanctioned_by = request.POST.get(f'Sanctioned_by{i}')
                            Position = request.POST.get(f'Position{i}')
                            Applied_dates = request.POST.get(f'Applied_dates{i}')
                            Sanctioned_date = request.POST.get(f'Sanctioned_date{i}')
                            Total_amount_sanctioned = request.POST.get(f'Total_amount_sanctioned{i}')
                            Amount_received = request.POST.get(f'Amount_received{i}')
                            projects_sanctioned_detials[label] = {
                                f'Title_of_projects{i}': Title_of_projects, 
                                f'Sanctioned_by{i}': Sanctioned_by, 
                                f'Position{i}': Position,
                                f'Applied_dates{i}': Applied_dates,
                                f'Sanctioned_date{i}': Sanctioned_date,
                                f'Total_amount_sanctioned{i}': Total_amount_sanctioned,
                                f'Amount_received{i}': Amount_received
                            }
                    else:
                        projects_sanctioned_detials = {}

                    Awarda = request.POST.get('award_detials')
                    number_a = request.POST.get('number_a')
                    if Awarda == "yes":
                        num_a = int(number_a)
                        Award = {}
                        for i in range(1, num_a + 1):
                            label = f'Award {i}'
                            Name_of_the_award = request.POST.get(f'Name_of_the_award{i}')
                            Title_of_the_awards = request.POST.get(f'Title_of_the_awards{i}')
                            Issued_by = request.POST.get(f'Issued_by{i}')
                            Received_Date = request.POST.get(f'Received_Date{i}')
                            Award[label] = {
                                f'Name_of_the_award{i}': Name_of_the_award, 
                                f'Title_of_the_awards{i}': Title_of_the_awards, 
                                f'Issued_by{i}': Issued_by,
                                f'Received_Date{i}': Received_Date
                            }
                    else:
                        Award = {}

                    Membership = request.POST.get('Membership_in_professional_bodies_Detials')
                    number_m = request.POST.get('number_m')
                    if Membership == "yes":
                        num_m = int(number_m)
                        Membership_in_professional_bodies_Detials = {}
                        for i in range(1, num_m + 1):
                            label = f'Membership_in_professional_bodies_Detials {i}'
                            Name_of_professional_chapter = request.POST.get(f'Name_of_professional_chapter{i}')
                            Year_of_registration = request.POST.get(f'Year_of_registration{i}')
                            validity = request.POST.get(f'membership_validity{i}')
                            Membership_in_professional_bodies_Detials[label] = {
                                f'Name_of_professional_chapter{i}': Name_of_professional_chapter, 
                                f'Year_of_registration{i}': Year_of_registration,
                                f'membership_validity{i}': validity
                            }
                    else:
                        Membership_in_professional_bodies_Detials = {}
                    
                    Recognised_as_Research_Supervisor = request.POST.get('Recognised_as_Research_Supervisor')
                    if Recognised_as_Research_Supervisor == "yes":
                        recognized_by = request.POST.get('Recognised_by')
                        year_recognition = request.POST.get('Yr_of_Recognised')
                        scholars_completed = request.POST.get('No_of_scholar_completed')
                        scholars_guiding = request.POST.get('No_of_scholar_guiding')
                        full_time_scholars = request.POST.get('No_of_full_time_scholar')
                        part_time_scholars = request.POST.get('No_of_part_time_scholar')
                        internal_scholars = request.POST.get('No_of_internal_scholar')
                        external_scholars = request.POST.get('No_of_external_scholar')
                    else:
                        recognized_by = year_recognition = scholars_completed = scholars_guiding = full_time_scholars = part_time_scholars = internal_scholars = external_scholars = None

                    #save data
                    data = detail(
                            campus = campus,
                            college_name = college_name,
                            email_address = email_address,
                            employee_id = employee_id,
                            department = department,
                            name_of_faculty = name_of_faculty,
                            gender = gender,
                            date_of_birth = date_of_birth,
                            designation = designation,
                            year_of_joining = year_of_joining,
                            srm_experience = srm_experience,
                            other_college_experience = other_college_experience,
                            industry_experience = industry_experience,
                            Passport_size_photo = Passport_size_photo,

                            ug = ug,
                            ug_university = ug_university,
                            ug_place = ug_place,
                            ug_percentage = ug_percentage,
                            ug_mode = ug_mode,
                            ug_parttime_mode = ug_parttime_mode,
                            ug_period = ug_period,
                            ug_class = ug_class,
                            ug_ur = ug_ur,
                            ug_cr = ug_cr,

                            pg = pg,
                            pg_university = pg_university,
                            pg_place = pg_place,
                            pg_percentage = pg_percentage,
                            pg_mode =pg_mode,
                            pg_parttime_mode = pg_parttime_mode,
                            pg_period = pg_period,
                            pg_class = pg_class,
                            pg_ur = pg_ur,
                            pg_cr = pg_cr,

                            phd = phd,
                            phd_university = phd_university,
                            phd_place = phd_place,
                            phd_duration = phd_duration,
                            phd_percentage = phd_percentage,
                            year_of_completion = year_of_completion,
                            phd_mode = phd_mode,
                            phd_fulltime_mode = phd_fulltime_mode,
                            diploma = diploma,

                            name_of_course = name_of_course,
                            university_for_course = university_for_course,
                            diploma_percentage = diploma_percentage,
                            diploma_class = diploma_class,

                            research_area = research_area,
                            total_indexed_papers = total_indexed_papers,
                            ugc_care_papers = ugc_care_papers,
                            scopus_papers = scopus_papers,
                            web_of_science_papers = web_of_science_papers,
                            sci = sci,
                            national_conf_presented = national_conf_presented,
                            conference_proceedings_isbn = conference_proceedings_isbn,

                            patent_detials = patent,
                            book_detials = book,
                            fdp_detials = fdp,
                            workshop_detials = workshop,
                            project_detials = Projects,
                            project_sanctioned_detials = projects_sanctioned_detials,
                            award_detials = Award,
                            Membership_in_professional_bodies_Detials = Membership_in_professional_bodies_Detials,

                            Recognised_as_Research_Supervisor = Recognised_as_Research_Supervisor,
                            recognized_by = recognized_by,
                            year_recognition = year_recognition,
                            scholars_completed = scholars_completed,
                            scholars_guiding = scholars_guiding,
                            full_time_scholars = full_time_scholars,
                            part_time_scholars = part_time_scholars,
                            internal_scholars = internal_scholars,
                            external_scholars = external_scholars,
                    )
                    data.save()
                    return redirect('home')
                return render(request, 'get_data.html', {
                    'data': data,
                    'favicon': favicon_src,
                    'logo': logo_src
                })
        except staff.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')

    
def logout(request):
    request.session.clear()
    return redirect('login')    

def s(request):
    user = details.objects.get(Employee_id='dk1')
    return render(request, 'home.html', {'name': user.name, 'des':user.Designation, 'dob':user.dob, 'exp':user.exp, 'srm_exp':user.srm_exp, 'email': user.email_address, 'img':user.img, 'favicon':favicon_src})    


def edit_profile(request, employee_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        deta = detail.objects.get(employee_id=employee_id)
        print("pn",len(deta.patent_detials))
        if request.method == 'POST':
            campus = request.POST.get('campus')
            college_name = request.POST.get('college_name')
            email_address = request.POST.get('Email_Address')
            employee_id = request.POST.get('Employee_id')
            department = request.POST.get('Department')
            name_of_faculty = request.POST.get('Name_of_the_faculty')
            gender = request.POST.get('Gender')
            date_of_birth = request.POST.get('Date_of_Birth')
            designation = request.POST.get('Designation')
            year_of_joining = request.POST.get('Year_of_joining')
            srm_experience = request.POST.get('SRM_experience_Year')
            other_college_experience = request.POST.get('Other_college_experience_Year')
            industry_experience = request.POST.get('industry_experience')
            image = request.FILES.get('image_file')
            if image:
                Passport_size_photo = b64encode(image.read()).decode("utf-8")
            else:
                Passport_size_photo = deta.Passport_size_photo

            ug = request.POST.get('ug')
            ug_university = request.POST.get('Name_of_the_Universityug')
            ug_place = request.POST.get('ug_place')
            ug_percentage = request.POST.get('ug_percentage')
            ug_mode = request.POST.get('ugmode')
            if ug_mode == 'Part-time':
                ug_parttime_mode = request.POST.get('parttime_modeug')
            else:
                ug_parttime_mode = ""

            ug_period = request.POST.get('ug_period')
            ug_class = request.POST.get('ugclass')
            if ug_class == '1st Class with Distinction':
                ug_ur = request.POST.get('ug_university_rank')
                ug_cr = request.POST.get('ug_college_rank')
            else:
                ug_ur = ""
                ug_cr = ""
            
            pg = request.POST.get('pg')
            pg_university = request.POST.get('Name_of_the_Universitypg')
            pg_place = request.POST.get('ug_place')
            pg_percentage = request.POST.get('pg_percentage')
            pg_mode = request.POST.get('pgmode')
            if pg_mode == 'Part-time':
                pg_parttime_mode = request.POST.get('parttime_modepg')
            else:
                pg_parttime_mode = ""
            
            pg_period = request.POST.get('pg_period')
            pg_class = request.POST.get('pgclass')
            if pg_class == '1st Class with Distinction':
                pg_ur = request.POST.get('pg_university_rank')
                pg_cr = request.POST.get('pg_college_rank')
            else:
                pg_ur = ""
                pg_cr = ""

            phd = request.POST.get('phd')
            phd_university = request.POST.get('Name_of_the_Universityphd')
            phd_place = request.POST.get('phd_place')
            phd_duration = request.POST.get('phd_Duration')
            phd_percentage = request.POST.get('phd_percentage')
            year_of_completion = request.POST.get('Year_of_completion')
            phd_mode = request.POST.get('phdmode')
            if phd_mode == "Full-time":
                phd_fulltime_mode = request.POST.get('fulltime_modephd')
            else:
                phd_fulltime_mode = ""

            diploma = request.POST.get('Diploma')

            name_of_course = request.POST.get('name_of_the_cource')
            university_for_course = request.POST.get('Name_of_the_college')
            diploma_percentage = request.POST.get('diploma_Percentage')
            diploma_class = request.POST.get('dclass')

            research_area = request.POST.get('Research_Area')
            total_indexed_papers = request.POST.get('Total_No_of_papers_published')
            ugc_care_papers = request.POST.get('No_of_Papers_Published_in_UGC_Care_Journal')
            scopus_papers = request.POST.get('No_of_Papers_Published_in_Scopus_Indexed_Journal')
            web_of_science_papers = request.POST.get('No_of_Papers_Published_in_Web_of_Science_Journal')
            sci = request.POST.get('SCI')
            national_conf_presented = request.POST.get('No_of_National_Conference_Presented')
            conference_proceedings_isbn = request.POST.get('No_of_papers_published_in_conference_proceedings_with_ISBN_number')

            Patentp = request.POST.get('Patent')
            number_p = request.POST.get('number')
            if Patentp == "yes":
                num_p = int(number_p)
                patent_N = {}
                for i in range(len(deta.patent_detials), num_p + 1):
                    label = f'Patent {i}'
                    Patent_name = request.POST.get(f'patent_name{i}')
                    Patent_investieater = request.POST.get(f'investieater{i}')
                    # Patent_commercialized = request.POST.get(f'Patent_commercialized{i}')
                    Patent_status = request.POST.get(f'Patent_status{i}')
                    patent_N[label] = {
                        f'Patent_name{i}': Patent_name,
                        f'Patent_investieater{i}': Patent_investieater,
                        # f'Patent_commercialized{i}': Patent_commercialized,
                        f'Patent_status{i}': Patent_status
                    }
                
                patent = deta.patent_detials
                patent.update(patent_N)
            else:
                patent = deta.patent_detials
            
            bookb = request.POST.get('Books')
            number_b = request.POST.get('number_b')
            if bookb == "yes":
                num_b = int(number_b)
                book_n = {}
                for i in range(len(deta.book_detials), num_b + 1):
                    label = f'Book {i}'
                    Book_Title = request.POST.get(f'Book_Title{i}')
                    Book_publisher_name = request.POST.get(f'Book_publisher_name{i}')
                    isbn_number = request.POST.get(f'isbn_number{i}')
                    Year_of_publication = request.POST.get(f'Year_of_publication{i}')
                    Chapters = request.POST.get(f'Chapters{i}')
                    book_n[label] = {
                        f'Book_Title{i}': Book_Title, 
                        f'Book_publisher_name{i}': Book_publisher_name,
                        f'isbn_number{i}': isbn_number, 
                        f'Year_of_publication{i}': Year_of_publication,
                        f'Chapters{i}': Chapters
                    }
                
                book = deta.book_detials
                book.update(book_n)
            else:
                book = deta.book_detials
            
            fdpa = request.POST.get('fdp_attended')
            number_f = request.POST.get('number_f')
            if fdpa == "yes":
                num_f = int(number_f)
                fdp_n = {}
                for i in range(len(deta.fdp_detials), num_f + 1):
                    label = f'FDP {i}'
                    Name_of_the_fdp = request.POST.get(f'Name_of_the_fdp{i}')
                    Duration = request.POST.get(f'Duration{i}')
                    Organized_by = request.POST.get(f'Organized_by{i}')
                    Sponsored_by = request.POST.get(f'Sponsored_by{i}')
                    mode = request.POST.get(f'mode{i}')
                    fdp_n[label] = {
                        f'Name_of_the_fdp{i}': Name_of_the_fdp, 
                        f'Duration{i}': Duration, 
                        f'Organized_by{i}': Organized_by,
                        f'Sponsored_by{i}': Sponsored_by,
                        f'mode{i}': mode
                    }
                
                fdp = deta.fdp_detials
                fdp.update(fdp_n)
            else:
                fdp = deta.fdp_detials

            workshopa = request.POST.get('workshop_attended')
            number_w = request.POST.get('number_w')
            if workshopa == "yes":
                num_w = int(number_w)
                workshop_n = {}
                for i in range(len(deta.workshop_detials), num_w + 1):
                    label = f'workshop {i}'
                    Name_of_the_workshop = request.POST.get(f'Name_of_the_workshop{i}')
                    Duration = request.POST.get(f'Duration{i}')
                    Organized_by = request.POST.get(f'Organized_by{i}')
                    Sponsored_by = request.POST.get(f'Sponsored_by{i}')
                    mode = request.POST.get(f'mode{i}')
                    workshop_n[label] = {
                        f'Name_of_the_workshop{i}': Name_of_the_workshop, 
                        f'Duration{i}': Duration, 
                        f'Organized_by{i}': Organized_by,
                        f'Sponsored_by{i}': Sponsored_by,
                        f'mode{i}': mode
                    }
                
                workshop = deta.workshop_detials
                workshop.update(workshop_n)
            else:
                workshop = deta.workshop_detials

            Projectsa = request.POST.get('projects_detials')
            number_pr = request.POST.get('number_pr')
            if Projectsa == "yes":
                num_pr = int(number_pr)
                Projects_n = {}
                for i in range(len(deta.project_detials), num_pr + 1):
                    label = f'Projects {i}'
                    Title_of_project = request.POST.get(f'Title_of_project{i}')
                    Applied_to = request.POST.get(f'Applied_to{i}')
                    Applied_Date = request.POST.get(f'Applied_Date{i}')
                    Projects_n[label] = {
                        f'Title_of_project{i}': Title_of_project, 
                        f'Applied_to{i}': Applied_to, 
                        f'Applied_Date{i}': Applied_Date
                    }
                
                Projects = deta.project_detials
                Projects.update(Projects_n)
            else:
                Projects = deta.project_detials

            Projectss = request.POST.get('projects_sanctioned_detials')
            number_prs = request.POST.get('number_prs')
            if Projectss == "yes":
                num_prs = int(number_prs)
                projects_sanctioned_detials_n = {}
                for i in range(len(deta.project_sanctioned_detials), num_prs + 1):
                    label = f'projects_sanctioned_detials {i}'
                    Title_of_projects = request.POST.get(f'Title_of_projects{i}')
                    Sanctioned_by = request.POST.get(f'Sanctioned_by{i}')
                    Position = request.POST.get(f'Position{i}')
                    Applied_dates = request.POST.get(f'Applied_dates{i}')
                    Sanctioned_date = request.POST.get(f'Sanctioned_date{i}')
                    Total_amount_sanctioned = request.POST.get(f'Total_amount_sanctioned{i}')
                    Amount_received = request.POST.get(f'Amount_received{i}')
                    projects_sanctioned_detials_n[label] = {
                        f'Title_of_projects{i}': Title_of_projects, 
                        f'Sanctioned_by{i}': Sanctioned_by, 
                        f'Position{i}': Position,
                        f'Applied_dates{i}': Applied_dates,
                        f'Sanctioned_date{i}': Sanctioned_date,
                        f'Total_amount_sanctioned{i}': Total_amount_sanctioned,
                        f'Amount_received{i}': Amount_received
                    }
                
                projects_sanctioned_detials = deta.project_sanctioned_detials
                projects_sanctioned_detials.update(projects_sanctioned_detials_n)
            else:
                projects_sanctioned_detials = deta.project_sanctioned_detials

            Awarda = request.POST.get('award_detials')
            number_a = request.POST.get('number_a')
            if Awarda == "yes":
                num_a = int(number_a)
                Award_n = {}
                for i in range(len(deta.award_detials), num_a + 1):
                    label = f'Award {i}'
                    Name_of_the_award = request.POST.get(f'Name_of_the_award{i}')
                    Title_of_the_awards = request.POST.get(f'Title_of_the_awards{i}')
                    Issued_by = request.POST.get(f'Issued_by{i}')
                    Received_Date = request.POST.get(f'Received_Date{i}')
                    Award_n[label] = {
                        f'Name_of_the_award{i}': Name_of_the_award, 
                        f'Title_of_the_awards{i}': Title_of_the_awards, 
                        f'Issued_by{i}': Issued_by,
                        f'Received_Date{i}': Received_Date
                    }
                
                Award = deta.award_detials
                Award.update(Award_n)
            else:
                Award = deta.award_detials

            Membership = request.POST.get('Membership_in_professional_bodies_Detials')
            number_m = request.POST.get('number_m')
            if Membership == "yes":
                num_m = int(number_m)
                Membership_in_professional_bodies_Detials_n = {}
                for i in range(len(deta.Membership_in_professional_bodies_Detials), num_m + 1):
                    label = f'Membership_in_professional_bodies_Detials {i}'
                    Name_of_professional_chapter = request.POST.get(f'Name_of_professional_chapter{i}')
                    Year_of_registration = request.POST.get(f'Year_of_registration{i}')
                    validity = request.POST.get(f'membership_validity{i}')
                    Membership_in_professional_bodies_Detials_n[label] = {
                        f'Name_of_professional_chapter{i}': Name_of_professional_chapter, 
                        f'Year_of_registration{i}': Year_of_registration,
                        f'membership_validity{i}': validity
                    }
                
                Membership_in_professional_bodies_Detials = deta.Membership_in_professional_bodies_Detials
                Membership_in_professional_bodies_Detials.update(Membership_in_professional_bodies_Detials_n)
            else:
                Membership_in_professional_bodies_Detials = deta.Membership_in_professional_bodies_Detials
            
            Recognised_as_Research_Supervisor = request.POST.get('Recognised_as_Research_Supervisor')
            if Recognised_as_Research_Supervisor == "yes":
                recognized_by = request.POST.get('Recognised_by')
                year_recognition = request.POST.get('Yr_of_Recognised')
                scholars_completed = request.POST.get('No_of_scholar_completed')
                scholars_guiding = request.POST.get('No_of_scholar_guiding')
                full_time_scholars = request.POST.get('No_of_full_time_scholar')
                part_time_scholars = request.POST.get('No_of_part_time_scholar')
                internal_scholars = request.POST.get('No_of_internal_scholar')
                external_scholars = request.POST.get('No_of_external_scholar')
            else:
                recognized_by = year_recognition = scholars_completed = scholars_guiding = full_time_scholars = part_time_scholars = internal_scholars = external_scholars = None
            
            deta.campus = campus
            deta.college_name = college_name
            deta.email_address = email_address
            deta.employee_id = employee_id
            deta.department = department
            deta.name_of_faculty = name_of_faculty
            deta.gender = gender
            deta.date_of_birth = date_of_birth
            deta.designation = designation
            deta.year_of_joining = year_of_joining
            deta.srm_experience = srm_experience
            deta.other_college_experience = other_college_experience
            deta.industry_experience = industry_experience
            deta.Passport_size_photo = Passport_size_photo
            deta.ug = ug
            deta.ug_university = ug_university
            deta.ug_place = ug_place
            deta.ug_percentage = ug_percentage
            deta.ug_mode = ug_mode
            deta.ug_parttime_mode = ug_parttime_mode
            deta.ug_period = ug_period
            deta.ug_class = ug_class
            deta.ug_ur = ug_ur
            deta.ug_cr = ug_cr
            deta.pg = pg
            deta.pg_university = pg_university
            deta.pg_place = pg_place
            deta.pg_percentage = pg_percentage
            deta.pg_mode = pg_mode
            deta.pg_parttime_mode = pg_parttime_mode
            deta.pg_period = pg_period
            deta.pg_class = pg_class
            deta.pg_ur = pg_ur
            deta.pg_cr = pg_cr
            deta.phd = phd
            deta.phd_university = phd_university
            deta.phd_place = phd_place
            deta.phd_duration = phd_duration
            deta.phd_percentage = phd_percentage
            deta.year_of_completion = year_of_completion
            deta.phd_mode = phd_mode
            deta.phd_fulltime_mode = phd_fulltime_mode
            deta.diploma = diploma
            deta.name_of_course = name_of_course
            deta.university_for_course = university_for_course
            deta.diploma_percentage = diploma_percentage
            deta.diploma_class = diploma_class
            deta.research_area = research_area
            deta.total_indexed_papers = total_indexed_papers
            deta.ugc_care_papers = ugc_care_papers
            deta.scopus_papers = scopus_papers
            deta.web_of_science_papers = web_of_science_papers
            deta.sci = sci
            deta.national_conf_presented = national_conf_presented
            deta.conference_proceedings_isbn = conference_proceedings_isbn
            deta.Recognised_as_Research_Supervisor = Recognised_as_Research_Supervisor
            deta.recognized_by = recognized_by
            deta.year_recognition = year_recognition
            deta.scholars_completed = scholars_completed
            deta.scholars_guiding = scholars_guiding
            deta.full_time_scholars = full_time_scholars
            deta.part_time_scholars = part_time_scholars
            deta.internal_scholars = internal_scholars
            deta.external_scholars = external_scholars


            deta.patent_detials = patent
            deta.book_detials = book
            deta.fdp_detials = fdp
            deta.workshop_detials = workshop
            deta.project_detials = Projects
            deta.project_sanctioned_detials = projects_sanctioned_detials
            deta.award_detials = Award
            deta.Membership_in_professional_bodies_Detials = Membership_in_professional_bodies_Detials
            deta.save()
            return redirect("edit_profile", employee_id=deta.employee_id)
        pn_len = len(deta.patent_detials)
        bn_len = len(deta.book_detials)
        fn_len = len(deta.fdp_detials)
        wn_len = len(deta.workshop_detials)
        pd_len = len(deta.project_detials)
        psn_len = len(deta.project_sanctioned_detials)
        an_len = len(deta.award_detials)
        mn_len = len(deta.Membership_in_professional_bodies_Detials)

        return render(request,"edit_profile.html", 
                          {"data":deta, 
                           "pn":pn_len, 
                           "bn":bn_len,
                           "fn":fn_len,
                           "wn":wn_len,
                           "pn":pn_len,
                           "psn":psn_len,
                           "an":an_len,
                           "mn":mn_len,
                           "favicon": favicon_src,
                           "logo": logo_src})
    else:
        return redirect('login')