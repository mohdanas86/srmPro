from djongo.models import Model, ObjectIdField, CharField, IntegerField

class src(Model):
    name = CharField(max_length=100)
    image = CharField(max_length=200000)

class details(Model):
    Employee_id = CharField(max_length=100)
    Designation = CharField(max_length=100)
    email_address = CharField(max_length=100, db_column='Email Address')
    name = CharField(max_length=100, db_column='Name of the faculty')
    Designation = CharField(max_length=100)
    dob = CharField(max_length=100, db_column='Date of Birth')
    exp = CharField(max_length=100, db_column='Other college experience Year( years, Months )')
    srm_exp = CharField(max_length=100, db_column='SRM experience Year( years, Months )')
    img = CharField(max_length=100,db_column='Passport size photo (Formal photo)')
    Department = CharField(max_length=100, db_column='Department')

class staff(Model):
    _id = ObjectIdField()
    Employee_id = CharField(max_length=100)
    name = CharField(max_length=100)
    password = CharField(max_length=128)
    email = CharField(max_length=100) 
    Department = CharField(max_length=100)
    Designation = CharField(max_length=100)

    
