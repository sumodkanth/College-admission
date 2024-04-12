from datetime import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from AdminUI.models import StudentDB, DepartmentDB, CourseDB, JobsDB, JobApplications, newsDB, placed_studdb, Marquee, \
    newsDB2, InterviewStep, JobStatus2,TrainingDB,FacultyEnrollmentDB,CourseenrollmentDB, MultipleChoiceQuestion, Choice, TestResult,Payment
from .forms import SelectionStatusForm
from django.contrib.auth.decorators import login_required
import FacultyUI.views
import AdminUI.views
import random

from django.conf import settings
from django.core.mail import send_mail
from django_otp import user_has_device
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from AdminUI.models import JobApplications
from django.http import HttpResponse
from django.views.decorators.cache import never_cache


# Create your views here.x
def redirect_authenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.path == reverse(main_login):
            return redirect(main_login)
        return view_func(request, *args, **kwargs)
    return wrapper

@never_cache
def main_login(request):
    if request.session.get('username'):
        return redirect('main_page')
    else:
      return render(request, "main_login.html")

# def main_login(request):
#     if request.session.get('logged_in', False):
#         # If the user is already logged in, redirect to the main page
#         return redirect('main_page')
#
#     if "username" in request.session:
#         username = request.session["username"]
#         try:
#             student = StudentDB.objects.get(StudentId=username)
#             # Assuming 'main_page' is the name of the URL pattern for the main page
#             return redirect('main_page')
#         except StudentDB.DoesNotExist:
#             # Handle the case where the user is not found in the database
#             return render(request, "main_login.html")
#     else:
#         # Handle the case where the user is not logged in
#         return render(request, "main_login.html")






@redirect_authenticated_user
def main_page(request):

            stud_email = request.session.get("username")
            last_post = newsDB.objects.latest('newsId')
            recent_posts = newsDB.objects.order_by('newsId')[0:5]
            last_post2 = newsDB2.objects.latest('newsId')
            recent_posts2 = newsDB2.objects.order_by('newsId')[0:5]
            job_data = JobsDB.objects.all()
            placed_posts = placed_studdb.objects.order_by('p_id')[0:30]
            marquee_texts = Marquee.objects.all()

            if  stud_email:
                name = StudentDB.objects.get(Email=stud_email)
                return render(request, "main_home.html",
                              {"name": name, "job_data": job_data, "last_post": last_post, "last_post2": last_post2,
                               "recent_posts": recent_posts, "recent_posts2": recent_posts2,
                               "placed_posts": placed_posts, 'marquee_texts': marquee_texts})
            else:
                return render(request, "main_home.html",
                              {"job_data": job_data, "last_post": last_post, "last_post2": last_post2,
                               "recent_posts": recent_posts, "recent_posts2": recent_posts2,
                               "placed_posts": placed_posts, 'marquee_texts': marquee_texts})


def recruiter(request):
    stud_id = request.session.get("username")
    job_data = JobsDB.objects.all()
    if stud_id:
        name = StudentDB.objects.get(Email=stud_id)
        return render(request, "1_recruiter.html", {"name": name, 'job_data': job_data})
    else:
        return render(request, "1_recruiter.html", {'job_data': job_data})


def placement(request):
    stud_id = request.session.get("username")
    if stud_id:
        name = StudentDB.objects.get(Email=stud_id)
        return render(request, "2_placement.html", {"name": name})
    else:
        return render(request, "2_placement.html")


def training(request):
    # stud_id = request.session["username"]
    # name = StudentDB.objects.get(StudentId=stud_id)
    return render(request, "3_trainingt.html")


def gallery(request):
    if 'username' in request.session:
        stud_id = request.session["username"]
        name = StudentDB.objects.get(Email=stud_id)
        return render(request, "4_gallery.html",{'name':name})
    else:
        return render(request, "4_gallery.html")


def contact(request):
    if 'username' in request.session:
        stud_id = request.session["username"]
        name = StudentDB.objects.get(Email=stud_id)
        return render(request, "6_contact.html",{'name':name})
    else:
        return render(request, "6_contact.html")


def indexpage(request):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(Email=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request, "studentindex.html", {'name': name, 'course': course, 'dept': dept})


def stud_profile(request):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(Email=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request, "student_profile.html", {'name': name, 'course': course, 'dept': dept})


def stud_edit(request):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(Email=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request, "student_edit.html", {'name': name, 'course': course, 'dept': dept})


def stud_save(request):
    if request.method == "POST":
        stud_id = request.POST.get('StudentId')
        stud_fname = request.POST.get('FirstName')
        stud_lname = request.POST.get('LastName')
        stud_dob = request.POST.get('DateOfBirth')
        date_objj = datetime.strptime(stud_dob, "%B %d, %Y")
        formatted_dob = date_objj.strftime("%Y-%m-%d")
        stud_gender = request.POST.get('Gender')
        stud_email = request.POST.get('Email')
        stud_mob = request.POST.get('ContactNo')
        stud_address = request.POST.get('Address')
        stud_gcontact = request.POST.get('GuardianContact')
        stud_gname = request.POST.get('GuardianName')
        stud_dept = request.POST.get('DeptName')
        stud_course = request.POST.get('CourseName')
        pa = request.POST.get("Pancard")
        adhar = request.POST.get("adhaar")
        try:
            stud_image = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(stud_image.name, stud_image)
        except MultiValueDictKeyError:
            file = StudentDB.objects.get(StudentId=stud_id).Image
            print(file)
        if StudentDB.objects.filter(StudentId=stud_id).exists():
            StudentDB.objects.filter(StudentId=stud_id).update(FirstName=stud_fname, LastName=stud_lname,
                                                               DateOfBirth=formatted_dob, Gender=stud_gender,
                                                               Email=stud_email, ContactNo=stud_mob,
                                                               Address=stud_address,
                                                               GuardianContact=stud_gcontact, GuardianName=stud_gname,
                                                               Image=file, Pancard=pa, adhaar=adhar)
        else:
            stud_image = request.FILES['Image']
            obj = StudentDB(FirstName=stud_fname, LastName=stud_lname,
                            DateOfBirth=stud_dob, Gender=stud_gender,
                            Email=stud_email, ContactNo=stud_mob, Address=stud_address,
                            GuardianContact=stud_gcontact, GuardianName=stud_gname,
                            Image=stud_image, Pancard=pa, adhaar=adhar)
            obj.save()
        return redirect(stud_profile)


def stud_notification(request):
    if 'username' in request.session:
        stud_id = request.session["username"]
        name = StudentDB.objects.get(Email=stud_id)
        obj = newsDB.objects.all()
        return render(request, 'notification.html', {"obj": obj,'name':name})
    else:
        obj = newsDB.objects.all()
        return render(request, 'notification.html', {"obj": obj})


def stud_notification2(request):
    obj = newsDB2.objects.all()
    return render(request, 'notification2.html', {"obj": obj})


def stud_user(request):
    return render(request, 'student_login.html')

# @redirect_authenticated_user
def stud_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        stud_pwd = request.POST.get('password')

        if  StudentDB.objects.filter(Email=email, password=stud_pwd):
            request.session['username'] =  email
            request.session['password'] = stud_pwd
            messages.success(request, "Login successfully")
            return redirect(main_page)
        elif FacultyEnrollmentDB.objects.filter(Email=email, password=stud_pwd):
            request.session['username'] =  email
            request.session['password'] = stud_pwd
            messages.success(request, "Login successfully")
            return redirect('admin_indexpage')
        else:
            messages.error(request, "Invalid ID or Password")
            return redirect(main_login)


def stud_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(main_page)


def jobs_view(request):
    if 'username' in request.session:
        stud_id = request.session["username"]
        name = StudentDB.objects.get(Email=stud_id)
        job_data = JobsDB.objects.all()
        return render(request, "jobs_view.html", {'job_data': job_data,'name':name})
    else:
        job_data = JobsDB.objects.all()
        return render(request, "jobs_view.html", {'job_data': job_data})

def course_view(request):
    if 'username' in request.session:
        stud_id = request.session["username"]
        name = StudentDB.objects.get(Email=stud_id)
        course_data = CourseDB.objects.all()
        return render(request, "course_view.html", {'course_data': course_data,'name':name})
    else:
        course_data = CourseDB.objects.all()
        return render(request, "course_view.html", {'course_data': course_data})


def jobs_view_single(request, job_id):
    if 'username' in request.session:
        stud_id = request.session["username"]
        name =StudentDB.objects.get(Email=stud_id)
        job_data = JobsDB.objects.get(JobId=job_id)
        applied = JobApplications.objects.filter(JobId=job_id, Email=stud_id).exists()



        return render(request, "job_view_single.html",
                      {'job_data': job_data, 'applied': applied, 'name':name})
    else:
        messages.error(request, 'Please log in to view this page.')
        return render(request, "main_login.html")

def course_view_single(request, course_id):
    if 'username' in request.session:
        stud_id = request.session["username"]
        name =StudentDB.objects.get(Email=stud_id)
        course_data = CourseDB.objects.get(CourseId=course_id)
        applied = CourseenrollmentDB.objects.filter(Email=stud_id, CourseId=course_id).exists()

        return render(request, "course_view_single.html",
                      {'course_data': course_data, 'name':name,'applied':applied})
    else:
        messages.error(request, 'Please log in to view this page.')
        return render(request, "main_login.html")

def job_apply(request, job_id):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(Email=stud_id)
    job = JobsDB.objects.get(JobId=job_id)
    resume = request.FILES["resume"]
    obj = JobApplications(JobId=job, Email=name, Resume=resume)
    obj.save()
    return redirect(jobs_view)



def notification_single(request, news_ids):
    if 'username' in request.session:
        stud_id = request.session["username"]
        name = StudentDB.objects.get(Email=stud_id)
        news_data = newsDB.objects.get(newsId=news_ids)
        applied = TrainingDB.objects.filter(newsId=news_ids, Email=stud_id).exists()

        return render(request, "notification_single.html",
                      {"news_data": news_data, 'applied': applied, 'name': name})
    else:
        messages.error(request, 'Please log in to view this page.')
        return render(request, "main_login.html")

def notification_single2(request, news_id):
    news_data = newsDB2.objects.get(newsId=news_id)
    return render(request, "notification_single2.html", {"news_data": news_data})


def help(request):
    # if 'username' in request.session:
    #     stud_id = request.session["username"]
    #     name = StudentDB.objects.get(StudentId=stud_id)
    #     return render(request, '5_help.html',{'name':name})
    # else:
        return render(request, '5_help.html')


def entermail1(request):
    return render(request, 'entermail1.html')


def generate_and_send_otp(request):
    if request.method == "POST":
        mailid1 = request.POST.get("mailid1")

        try:
            # Check if the email exists in the StudentDB model
            student = StudentDB.objects.get(Email=mailid1)
            messages.success(request, 'Please Check your Email')
        except StudentDB.DoesNotExist:
            messages.error(request, 'Email is not registered.')
            # If the email doesn't exist, handle the error or return a response
            return render(request, 'entermail1.html')  # Customize this template or response

        # Generate a random 6-digit OTP
        otp = str(random.randint(100000, 999999))
        request.session['otp'] = otp

        # Send the OTP via email
        subject = 'Your One-Time Password (OTP)'
        message = f'Your OTP is: {otp}'
        from_email = 'akshayasleepergirl@gmail.com'  # Update with your email
        to_email = [student.Email]

        # Use try-except for send_mail to handle potential email sending errors
        try:
            send_mail(subject, message, from_email, to_email)
        except Exception as e:
            # Handle the email sending error, log it, or redirect to an error page
            messages.error(request, 'Please Try Again.')
            return render(request, 'entermail1.html', {'error_message': str(e)})

        # Redirect to the enterotp1 view after sending the OTP
        return redirect(reverse('enterotp1') + f'?email={mailid1}')

    # Handle the case where the request method is not POST or any other condition
    return render(request, 'entermail1.html')  # Customize this template or response


def enterotp1(request):
    # Get the email value from the query parameters
    email = request.GET.get('email', None)

    # You can now use the 'email' variable in your template or view logic
    return render(request, 'enterotp1.html', {'email': email})


def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp1')
        email = request.POST.get('email1')
        stored_otp = request.session.get('otp')

        # Check if the email exists in the StudentDB model
        try:
            student = StudentDB.objects.get(Email=email)
        except StudentDB.DoesNotExist:
            # If the email doesn't exist, handle the error or return a response
            return render(request, 'email_not_found.html')  # Customize this template or response

        if stored_otp and entered_otp == stored_otp:
            # Store the email in the session for later use
            request.session['verified_email'] = email
            messages.success(request, 'OTP verified Successfully!!')
            return redirect('newpass')
        else:
            messages.error(request, 'Invalid OTP')
            return redirect('entermail1')

    return render(request, 'entermail1.html')


def newpass(request):
    # Retrieve the email from the session
    email = request.session.get('verified_email')
    if not email:
        # Handle the case where the email is not in the session
        return redirect('entermail1')  # Redirect to the entermail1 page or handle as needed

    # Use the email in your newpass view logic
    return render(request, 'newpass.html', {'email': email})


def update_password(request):
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        email = request.POST.get('email')

        # Check if passwords match
        if otp1 == otp2:
            # Assuming you have the student object available, update the password
            student = StudentDB.objects.get(Email=email)  # Replace this with how you get the student object

            # Update the password in the student model
            student.password = otp1
            student.save()

            messages.success(request, 'Password updated successfully!')
            return redirect('main_login')  # Replace 'home' with the appropriate URL name

        else:
            messages.error(request, 'Passwords do not match. Please try again.')

    return render(request, 'entermail1.html')  # Replace 'your_template.html' with the actual template name


@login_required
def selection_status_view(request):
    if request.method == 'POST':
        form = SelectionStatusForm(request.POST)
        if form.is_valid():
            selection_status = form.save(commit=False)
            selection_status.user = request.user  # Set the current user
            selection_status.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = SelectionStatusForm()
    return render(request, 'job_view_single.html', {'form': form})



def status_update(request, job_update, applied_student_id):
    job_data2 = JobsDB.objects.get(Company=job_update)
    job_steps = InterviewStep.objects.filter(job=job_data2)
    name = StudentDB.objects.get(FirstName=applied_student_id)
    # Fetch interview steps associated with the job
    # This assumes you have a foreign key relationship between JobsDB and InterviewStep

    return render(request, "statusupdate.html", {'job_data2': job_data2, 'job_steps': job_steps,'name':name})






def save_status(request):
    if request.method == 'POST':
        # Retrieve data from the form
        job_title = request.POST.get('job_title')
        company = request.POST.get('Company')
        student_name = request.POST.get('FirstName')  # Assuming this is the ID of the student associated with the job
        selected_step_id = request.POST.get('job_steps')
        course = request.POST.get('CourseName')
        # course_obj = get_object_or_404(CourseDB,CourseName=course)

        # Get or create the job object based on the title and company
        job, _ = JobsDB.objects.get_or_create(Title=job_title, Company=company)

        # Get or create the course object based on the course name
        course_obj = CourseDB.objects.get(CourseName=course)

        # Get or create the student object based on the student name
        student, _ = StudentDB.objects.get_or_create(FirstName=student_name)

        # Get the selected interview step object
        selected_step = InterviewStep.objects.get(id=selected_step_id)


        # Update or create a new job status associated with the job and selected step
        job_status, created = JobStatus2.objects.update_or_create(
            job=job,

            defaults={
                'status_text': selected_step.step_text,
                'Student': student.FirstName,
                'course' : course_obj

            }
        )

        # Redirect to a success page or do something else
        return redirect('jobs_view')  # Adjust the URL name as needed
    else:
        # Handle GET requests if needed
        pass

def applytraining(request,trainID):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(Email=stud_id)
    news = newsDB.objects.get(newsId=trainID)
    obj =TrainingDB(newsId=news, StudentId=name)
    obj.save()
    return redirect(stud_notification)

def student_registration(request):
  
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
      
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
       
        password = request.POST.get("password")
       
        obj = StudentDB(FirstName=fname, LastName=lname, 
                        DateOfBirth=dob, Gender=gender, Email=email, ContactNo=contact, password=password)
        obj.save()
        return redirect('main_login')

    return render(request,'student_signup.html')




def faculty_registration(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        endate = request.POST.get("date")
        dept = request.POST.get("dept")
        dept_data = DepartmentDB.objects.get(DeptName=dept)
        deptt = dept_data.DeptId
        contact = request.POST.get("contact")
        desig = request.POST.get("designation")
        status = request.POST.get("admin_status")
        password = request.POST.get("password")
        if status:
            obj = FacultyEnrollmentDB(Name=name,Email=email,password=password, Joined=endate, DeptId=dept_data, Designation=desig, Contact=contact,
                                      is_admin="True")
            obj.save()
        else:
            obj = FacultyEnrollmentDB(Name=name,password=password, Joined=endate,Email=email, DeptId=dept_data, Designation=desig, Contact=contact,
                                      is_admin="False")
            obj.save()

            return redirect('main_login')
    data = DepartmentDB.objects.all()
    return render(request,'faculty_signup.html',{'data':data})

def submission_form(request,course):
    if 'username' in request.session:
        stud_id = request.session["username"]
        course_data = CourseDB.objects.get(CourseName=course)
        name = StudentDB.objects.get(Email=stud_id)
        if request.method == "POST":
            return render(request, "submission_form.html",{'name':name,'course_data':course_data})
    else:
        messages.error(request, 'Please log in to view this page.')
        return redirect('main_login')

def course_submission(request):
    if request.method == "POST":

        sname = request.POST.get("student_name")
        contacts = request.POST.get("phone_number")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        coursee = request.POST.get("course")
        gender = request.POST.get("gender")
        religion = request.POST.get("rname")
        district = request.POST.get("dictname")
        address = request.POST.get("address")
        gname = request.POST.get("gname")
        plustwo = request.FILES["plus_two_certificate"]
        plustwomark = request.POST.get("plustwomark")
        sslc = request.FILES["sslc_certificate"]
        sslcmark = request.POST.get("sslcmark")
        im = request.FILES['img']
        course_data = CourseDB.objects.get(CourseName=coursee)



        obj = CourseenrollmentDB(StudentName=sname,  CourseId=course_data, Religion=religion,District=district,
                        DateOfBirth=dob, Gender=gender, Email=email, ContactNo=contacts, Address=address,
                        GuardianName=gname, Image=im,Plustwo=plustwo, SSLC=sslc, Plustwomark= plustwomark, SSLCMark= sslcmark)
        obj.save()
        return redirect(course_view)

    # views.py


def take_test(request, course_id):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(Email=stud_id)


    course = CourseDB.objects.get(CourseName=course_id)
    questions = list(MultipleChoiceQuestion.objects.filter(course=course))
    random.shuffle(questions)
    questions = questions[:5]  # Select five random questions

    if request.method == 'POST':
        score = 0
        for question in questions:
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                selected_choice = Choice.objects.get(pk=choice_id)
                if selected_choice.is_correct:
                    score += 1


        # Get or create the test result object for the student and course
        test_result, created = TestResult.objects.get_or_create(
            StudentName=name,
            course=course,
            defaults={'score': score}  # If creating, set default values
        )
        if not created:
            test_result.score = score
            test_result.save()

        # Send email to the user
        subject = 'Test Result'
        message = f'Hello {name},\n\nYour score for the {course.CourseName} test is: {score}. Your interview is scheduled for April 25th at 10.30 am in the college office.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [name.Email]  # Assuming email is stored in the Email field of the StudentDB model
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return redirect(course_view)

    context = {
        'course': course,
        'questions': questions,
        'name':name
    }
    return render(request, 'take_test.html', context)

def payment_page(request, course_id):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(Email=stud_id)
    name = CourseenrollmentDB.objects.get(Email=stud_id)
    # course = CourseDB.objects.get(CourseName=course_id)
    if request.method == 'POST':
        # Handle payment logic here using the provided payment details
        cardholder_name = request.POST.get('cardholder_name')
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv = request.POST.get('cvv')
        amount_received = request.POST.get('payable_amount')
        # Create payment associated with the order
        payment = Payment.objects.create(
            cardholder_name=cardholder_name,
            card_number=card_number,
            expiration_date=expiration_date,
            cvv=cvv,
            amount_received=amount_received,
            course=course,


        )

        # Associate the payment with the order
        course.payment = payment
        course.save()

        messages.success(request, 'Payment done successfully!')
        return redirect(studentindx)  # You can redirect or render a success page here
#hello
    context = {'course': course,
               'name':name}
    return render(request, 'payment.html', context)
