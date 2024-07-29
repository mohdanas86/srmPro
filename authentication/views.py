from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from .models import details, staff, src
from .import functions

logo = src.objects.get(name='logo')
favicon = src.objects.get(name='favicon icon')
logo_src = logo.image
favicon_src = favicon.image

def signup(request):
    if request.method == 'POST':
        Employee_id = request.POST.get('Employee_id')
        password = request.POST['password']
        re_pass = request.POST['re_pass']

        try:
            existing_staff = staff.objects.get(Employee_id=Employee_id)
            error = "Account already created"
            return render(request, 'signup.html', {'error': error,'logo':logo_src, 'favicon':favicon_src})
        except staff.DoesNotExist:
            try:
                user = details.objects.get(Employee_id=Employee_id)
                otp = functions.otp_verification(user.email_address)
                print(otp)

                if password == re_pass:
                    request.session['email'] = user.email_address
                    request.session['password'] = password
                    request.session['otp'] = otp
                    request.session['Employee_id'] = Employee_id
                    request.session['Department'] = user.Department
                    request.session['Designation'] = user.Designation
                    return redirect(reverse('otp_verify'))
                else:
                    error = "Password mismatch!"
                return render(request, 'signup.html', {'error': error,'logo':logo_src, 'favicon':favicon_src})
            except details.DoesNotExist:
                error = "Employee ID does not exist. Please contact the admin office."
                return render(request, 'signup.html', {'error': error,'logo':logo_src, 'favicon':favicon_src})
    return render(request, 'signup.html', {'logo':logo_src, 'favicon':favicon_src})

def otp_verify(request):
    if request.method == 'POST':
        Employee_id = request.session.get('Employee_id')
        email =  request.session.get('email')
        Department = request.session.get('Department')
        Designation = request.session.get('Designation')
        hashed_password = make_password(request.session['password'])
        otp = request.session['otp']
        e_otp = request.POST['otp']  
        if otp == e_otp:
            try:
                u = details.objects.get(Employee_id=Employee_id)
                user = staff(Employee_id=Employee_id, name=u.name, password=hashed_password, email=email, Department=Department, Designation=Designation)
                user.password = hashed_password
                user.save()
                return redirect(reverse('login') + '?message=Account created successfully')
            except details.DoesNotExist:
                error = "User does not exist. Please sign up."
                return render(request, 'otp_verification.html', {'email': email, 'error': error,'logo':logo_src, 'favicon':favicon_src})
        else:
            error = "Invalid OTP. Please try again."
            return render(request, 'otp_verification.html', {'email': email, 'error': error,'logo':logo_src, 'favicon':favicon_src})
    return render(request, 'otp_verification.html', {'logo':logo_src, 'favicon':favicon_src})

def forgot_password(request):
    if request.method == 'POST':
        Employee_id = request.POST.get('Employee_id')
        password = request.POST['password']
        re_pass = request.POST['re_pass']
        try:
            user = staff.objects.get(Employee_id=Employee_id)
            otp = functions.otp_verification(user.email)
            if password == re_pass:
                request.session['email'] = user.email
                request.session['password'] = password
                request.session['otp'] = otp
                return redirect(reverse('forgot_otp_verify'))
            else:
                error = "Password mismatch!"
            return render(request, 'forgot_password.html', {'error': error,'logo':logo_src, 'favicon':favicon_src})
        except staff.DoesNotExist:
            error = "User does not exist. Please sign up."
            return render(request, 'forgot_password.html', {'error': error,'logo':logo_src, 'favicon':favicon_src})
    return render(request, 'forgot_password.html',{'logo':logo_src, 'favicon':favicon_src})

def forgot_otp_verify(request):
    if request.method == 'POST':
        email =  request.session.get('email')
        hashed_password = make_password(request.session['password'])
        otp = request.session['otp']
        e_otp = request.POST['otp']  
        if otp == e_otp:
            try:
                user = staff.objects.get(email=email)
                user.password = hashed_password
                user.save()
                return redirect(reverse('login') + '?message=Password changed successfully')
            except staff.DoesNotExist:
                error = "User does not exist. Please sign up."
                return render(request, 'otp_verification.html', {'email': email, 'error': error,'logo':logo_src, 'favicon':favicon_src})
        else:
            error = "Invalid OTP. Please try again."
            return render(request, 'otp_verification.html', {'email': email, 'error': error,'logo':logo_src, 'favicon':favicon_src})
    return render(request, 'otp_verification.html', {'logo':logo_src, 'favicon':favicon_src})  

def login(request):
    if request.method == 'POST':
        Employee_id = request.POST['Employee_id']
        password = request.POST['password']
        try:
            user = staff.objects.get(Employee_id=Employee_id)
            if check_password(password, user.password):
                if user.Designation == 'HOD':
                    request.session['user_id'] = str(user._id)
                    return redirect('head')
                elif user.Designation == 'DEAN':
                    request.session['user_id'] = str(user._id)
                    return redirect('dean')
                else:
                    request.session['user_id'] = str(user._id)
                    return redirect('home')
            else:
                error = "Invalid credentials. Please try again."
                return render(request, 'login.html', {'error': error, 'logo':logo_src, 'favicon':favicon_src})
        except staff.DoesNotExist:
            error = "User does not exist. Please sign up."
            return render(request, 'login.html', {'error': error, 'logo':logo_src, 'favicon':favicon_src})

    if 'user_id' in request.session:
        return redirect('home')
    elif 'admin_id' in request.session:
        return redirect('admin')
    else:
        message = request.GET.get('message')
        return render(request, 'login.html', {'message': message, 'logo':logo_src, 'favicon':favicon_src})
    