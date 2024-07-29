from djongo.models import Model, ObjectIdField, CharField, IntegerField, JSONField

class detail(Model):
    _id = ObjectIdField()  
    campus = CharField(max_length=100)
    college_name = CharField(max_length=100)
    email_address = CharField(max_length=100)
    employee_id = CharField(max_length=50)
    department = CharField(max_length=100)
    name_of_faculty = CharField(max_length=100)
    gender = CharField(max_length=10)
    date_of_birth = CharField(max_length=100)
    designation = CharField(max_length=100)
    year_of_joining = IntegerField()
    srm_experience = CharField(max_length=100)
    other_college_experience = CharField(max_length=100)
    industry_experience = CharField(max_length=100)
    Passport_size_photo = CharField(max_length=100)
    
    # Educational Details
    ug = CharField(max_length=100)
    ug_university = CharField(max_length=100)
    ug_place = CharField(max_length=100)
    ug_percentage = CharField(max_length=100)
    ug_mode = CharField(max_length=100)
    ug_parttime_mode = CharField(max_length=100)
    ug_period = CharField(max_length=100)
    ug_class = CharField(max_length=100)
    ug_ur = CharField(max_length=100)
    ug_cr = CharField(max_length=100)

    pg = CharField(max_length=100)
    pg_university = CharField(max_length=100)
    pg_place = CharField(max_length=100)
    pg_percentage = CharField(max_length=100)
    pg_mode = CharField(max_length=100)
    pg_parttime_mode = CharField(max_length=100)
    pg_period = CharField(max_length=100)
    pg_class = CharField(max_length=100)
    pg_ur = CharField(max_length=100)
    pg_cr = CharField(max_length=100)

    phd = CharField(max_length=100)
    phd_university = CharField(max_length=100)
    phd_place = CharField(max_length=100)
    phd_duration = CharField(max_length=100)
    phd_percentage = CharField(max_length=100)
    year_of_completion = IntegerField()
    phd_mode =CharField(max_length=100)
    phd_fulltime_mode = CharField(max_length=100)

    diploma = CharField(max_length=100)
    
    # Diploma Details
    name_of_course = CharField(max_length=100)
    university_for_course = CharField(max_length=100)
    diploma_percentage = CharField(max_length=100)
    diploma_class = CharField(max_length=100)
    
    # Research Details
    research_area = CharField(max_length=100)
    total_indexed_papers = CharField(max_length=100)
    ugc_care_papers = CharField(max_length=100)
    scopus_papers = CharField(max_length=100)
    web_of_science_papers = CharField(max_length=100)
    sci = CharField(max_length=100)
    national_conf_presented = CharField(max_length=100)
    conference_proceedings_isbn = CharField(max_length=100)

    patent_detials = JSONField()
    book_detials = JSONField()
    fdp_detials = JSONField()
    workshop_detials = JSONField()
    project_detials = JSONField()
    project_sanctioned_detials = JSONField()
    award_detials = JSONField()
    Membership_in_professional_bodies_Detials =JSONField()

    Recognised_as_Research_Supervisor = CharField(max_length=100)
    recognized_by = CharField(max_length=100)
    year_recognition = IntegerField()
    scholars_completed = IntegerField()
    scholars_guiding = IntegerField()
    full_time_scholars = IntegerField()
    part_time_scholars = IntegerField()
    internal_scholars = IntegerField()
    external_scholars = IntegerField()