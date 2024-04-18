from django.contrib import admin
from .models import DepartmentDB, CourseDB, StudentDB, FacultyEnrollmentDB, JobsDB, placed_studdb,CourseenrollmentDB,MultipleChoiceQuestion,Choice,TestResult, Payment,HostelRoom,BusBooking,Booking,AdmissionDB

# Register your models here.
admin.site.register(DepartmentDB)
admin.site.register(CourseDB)
admin.site.register(StudentDB)
admin.site.register(FacultyEnrollmentDB)
admin.site.register(JobsDB)


admin.site.register(placed_studdb)



admin.site.register(CourseenrollmentDB)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(Choice)
admin.site.register(TestResult)
admin.site.register(Payment)
admin.site.register(HostelRoom)
admin.site.register(BusBooking)
admin.site.register(Booking)
admin.site.register(AdmissionDB)



