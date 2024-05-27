from django.db import models
from django.conf import settings
import pytz
from django.utils import timezone
# Create your models here.


class DepartmentDB(models.Model):
    DeptId = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length=100)
   
    def __str__(self):
        return self.DeptName

class CourseDB(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=20)
    DeptId = models.ForeignKey(DepartmentDB, on_delete=models.CASCADE,null=True,blank=True)
    Description = models.TextField()
    Duration = models.CharField(max_length=50, null=True, blank=True)
    Cost = models.CharField(max_length=20, null=True, blank=True)
    AdmissionFee = models.CharField(max_length=20, null=True, blank=True)
    Syllabus = models.FileField(upload_to='documents/', null=True, blank=True)
    def __str__(self):
        return self.CourseName


class StudentDB(models.Model):
    StudentId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200, null=True, blank=True)
    LastName = models.CharField(max_length=200, null=True, blank=True)
    DateOfBirth = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=1, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True,unique=True)
    ContactNo = models.IntegerField(blank=True, null=True)
    Address = models.TextField(null=True, blank=True)
    GuardianName = models.CharField(max_length=200, null=True, blank=True)
    GuardianContact = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="StudentsImage")
    EnrollmentID = models.CharField(max_length=20, null=True, blank=True)
    EnrollDate = models.DateField(null=True, blank=True)
    CourseId = models.ForeignKey(CourseDB, on_delete=models.CASCADE, null=True, blank=True)
    Pancard = models.CharField(max_length=50, null=True, blank=True)
    adhaar = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.Email


class FacultyEnrollmentDB(models.Model):
    Email = models.EmailField(max_length=200, null=True, blank=True,unique=True)
    FacultyID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Joined = models.DateField(null=True, blank=True)
    DeptId = models.ForeignKey(DepartmentDB, on_delete=models.CASCADE)
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Contact = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.Name

class JobsDB(models.Model):
    JobId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100, null=True, blank=True)
    Company = models.CharField(max_length=100, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=500, null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    image_job = models.ImageField(upload_to="job", null=True, blank=True)
    StudentId = models.ForeignKey(StudentDB, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.Title


class InterviewStep(models.Model):
    job = models.ForeignKey(JobsDB, on_delete=models.CASCADE)
    step_text = models.CharField(max_length=255)

    def __str__(self):
        return f"Step {self.pk} for {self.job.Title}"


class JobApplications(models.Model):
    JobId = models.ForeignKey(JobsDB, on_delete=models.CASCADE)
    # StudentId = models.ForeignKey(StudentDB, on_delete=models.CASCADE)
    Email = models.ForeignKey(StudentDB, on_delete=models.CASCADE)
    Resume = models.FileField(upload_to="Resume")


class newsDB(models.Model):
    newsId = models.AutoField(primary_key=True)
    news_Title = models.CharField(max_length=100, null=True, blank=True)
    news_Location = models.CharField(max_length=100, null=True, blank=True)
    news_date = models.DateField(null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    news_image = models.ImageField(upload_to="job", null=True, blank=True)
    def __str__(self):
        return self.news_Title

class newsDB2(models.Model):
    newsId = models.AutoField(primary_key=True)
    news_Title = models.CharField(max_length=100, null=True, blank=True)
    news_Location = models.CharField(max_length=100, null=True, blank=True)
    news_date = models.DateField(null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    news_image = models.ImageField(upload_to="job", null=True, blank=True)
    def __str__(self):
        return self.news_Title

class placed_studdb(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50, null=True, blank=True)
    p_company = models.CharField(max_length=50, null=True, blank=True)
    p_des = models.CharField(max_length=50, null=True, blank=True)
    p_dis = models.CharField(max_length=50, null=True, blank=True)
    p_img = models.ImageField(upload_to="placement", null=True, blank=True)
    def __str__(self):
        return self.p_name

class Marquee(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.text

class JobStatus2(models.Model):
    job = models.ForeignKey(JobsDB, on_delete=models.CASCADE, null=True, blank=True)
    status_text = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    Student = models.CharField(max_length=255, null=True, blank=True)
    course = models.ForeignKey(CourseDB, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Status: {self.status_text} "


class TrainingDB(models.Model):
    newsId = models.ForeignKey(newsDB, on_delete=models.CASCADE)
    # StudentId = models.ForeignKey(StudentDB, on_delete=models.CASCADE)
    Email = models.ForeignKey(StudentDB, on_delete=models.CASCADE)


class CourseenrollmentDB(models.Model):
    StudentName = models.CharField(max_length=100)
    CourseId = models.ForeignKey(CourseDB, on_delete=models.CASCADE)

    Religion = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=10)
    Email = models.EmailField()
    ContactNo = models.CharField(max_length=20)
    Address = models.TextField()
    GuardianName = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='images/')
    Plustwo = models.FileField(upload_to='documents/')
    SSLC = models.FileField(upload_to='documents/')
    Plustwomark = models.CharField(max_length=20)
    SSLCMark = models.CharField(max_length=20)
    # Add other fields as needed

    def __str__(self):
        return self.StudentName


class MultipleChoiceQuestion(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Question Text")
    course = models.ForeignKey(CourseDB, on_delete=models.CASCADE, verbose_name="Course")
    created_at = models.DateField(verbose_name="Created At",null=True, blank=True)
    def __str__(self):
        return self.question_text
    class Meta:
        verbose_name = "Multiple Choice Question"
        verbose_name_plural = "Multiple Choice Questions"


class Choice(models.Model):
    question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.choice_text} ({'Correct' if self.is_correct else 'Incorrect'})"


class TestResult(models.Model):
    StudentName = models.ForeignKey(StudentDB, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseDB, on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.score} "


class Payment(models.Model):
    student = models.ForeignKey(CourseenrollmentDB, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(CourseDB, on_delete=models.CASCADE,null=True, blank=True)
    rooms = models.ForeignKey('HostelRoom', on_delete=models.CASCADE,null=True, blank=True)
    bus = models.ForeignKey('BusBooking', on_delete=models.CASCADE,null=True, blank=True)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    cardholder_name = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100, null=True, blank=True)
    card_number = models.CharField(max_length=16,null=True, blank=True)
    expiration_date = models.CharField(max_length=7,null=True, blank=True)  # You might want to store this as a DateField if you need to perform date-related operations
    cvv = models.CharField(max_length=4,null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.amount_received} Paid"

class HostelRoom(models.Model):
    ROOM_TYPES = (
        ('single', 'Single'),
        ('shared', 'Shared'),
    )

    room_number = models.CharField(max_length=50)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    is_available = models.BooleanField(default=True)
    room_rent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.room_number}"


class Booking(models.Model):
    user = models.ForeignKey(CourseenrollmentDB, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(HostelRoom, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateField()
    def __str__(self):
        return f"{self.room}"




class BusBooking(models.Model):
    student_id = models.ForeignKey(StudentDB, on_delete=models.CASCADE, null=True, blank=True)
    student = models.CharField(max_length=100)

    pickup_location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    bus_fair = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class InterviewDB(models.Model):
    Email = models.EmailField(null=True, blank=True)
    StudentName = models.CharField(max_length=100,null=True, blank=True)
    CourseName = models.CharField(max_length=20,null=True, blank=True)
    InterviewStatus = models.CharField(max_length=10, choices=[('Passed', 'Passed'), ('Failed', 'Failed')], null=True, blank=True)
    # other fields

    def __str__(self):
        return self.Email

class AdmissionDB(models.Model):
    StudentName = models.CharField(max_length=100,null=True, blank=True)
    DateOfBirth = models.CharField(max_length=10,null=True, blank=True)
    Gender = models.CharField(max_length=10,null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    ContactNo = models.CharField(max_length=20,null=True, blank=True)
    CourseName = models.CharField(max_length=20,null=True, blank=True)
    # Add other fields as needed
    def __str__(self):
        return self.StudentName