from django.urls import path

from FacultyUI import views

urlpatterns = [
    path('faculty_index/', views.index_page, name="faculty_index"),
    path('faculty_profile/', views.profile_page, name="faculty_profile"),
    path('faculty_profile_edit/', views.profile_edit, name="faculty_profile_edit"),
    path('faculty_student_view/', views.students_view, name="faculty_student_view"),
    path('faculty_student_single/<int:dataid>/', views.student_single, name="faculty_student_single"),
    path('faculty_search_students/', views.search_students, name="faculty_search_students"),
    path('faculty_profile_save/', views.profile_save, name="faculty_profile_save"),
    path('faculty_logout/', views.faculty_logout, name="faculty_logout"),
    path('login_page/', views.login_page, name="login_page"),
    path('faculty_login/', views.faculty_login, name="faculty_login"),
    path('main-login2/', views.mainlogin2, name="main-login2"),

]
