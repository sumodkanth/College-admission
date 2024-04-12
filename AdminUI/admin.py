from django.contrib import admin
from .models import DepartmentDB, CourseDB, StudentDB, FacultyEnrollmentDB, JobsDB, InterviewStep, JobApplications, newsDB, newsDB2, placed_studdb, Marquee, JobStatus2,TrainingDB,CourseenrollmentDB,MultipleChoiceQuestion,Choice,TestResult

# Register your models here.
admin.site.register(DepartmentDB)
admin.site.register(CourseDB)
admin.site.register(StudentDB)
admin.site.register(FacultyEnrollmentDB)
admin.site.register(JobsDB)
admin.site.register(InterviewStep)
admin.site.register(JobApplications)
admin.site.register(newsDB)
admin.site.register(newsDB2)
admin.site.register(placed_studdb)
admin.site.register(Marquee)
admin.site.register(JobStatus2)
admin.site.register(TrainingDB)
admin.site.register(CourseenrollmentDB)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(Choice)
admin.site.register(TestResult)


