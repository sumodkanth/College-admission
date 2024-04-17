from django.urls import path

from Student import views
from django.contrib.auth import views as auth_views
from .views import selection_status_view
urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('recruiter/', views.recruiter, name="recruiter"),
    path('placement/', views.placement, name="placement"),
    path('training/', views.training, name="training"),
    path('gallery/', views.gallery, name="gallery"),
    path('help/', views.help, name="help"),
    path('contact/', views.contact, name="contact"),
    
    path('index/', views.indexpage, name="indexpage"),
    path('stud_profile/',views.stud_profile,name="stud_profile"),
    path('stud_edit/',views.stud_edit,name="stud_edit"),
    path('stud_save/',views.stud_save,name="stud_save"),
    path('stud_notification/',views.stud_notification,name="stud_notification"),
    path('stud_notification2/', views.stud_notification2, name="stud_notification2"),
    path('notification_single/<int:news_ids>',views.notification_single,name="notification_single"),
    path('notification_single2/<int:news_id>', views.notification_single2, name="notification_single2"),

    path('stud_user/',views.stud_user,name="stud_user"),
    path('stud_login/',views.stud_login,name="stud_login"),
    path('stud_save/',views.stud_save,name="stud_save"),
    path('stud_logout/',views.stud_logout,name="stud_logout"),
    path('jobs_view/', views.jobs_view, name="jobs_view"),
    path('course_view/', views.course_view, name="course_view"),
    path('jobs_view_single/<int:job_id>/', views.jobs_view_single, name="jobs_view_single"),
    path('course_view_single/<int:course_id>/', views.course_view_single, name="course_view_single"),
    path('job_apply/<int:job_id>/', views.job_apply, name="job_apply"),
    path('main_login/', views.main_login, name="main_login"),


    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_resetdone/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetdone/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('entermail1/',views.entermail1,name='entermail1'),
    path('generate_and_send_otp/',views.generate_and_send_otp,name='generate_and_send_otp'),
    path('enterotp1/',views.enterotp1,name='enterotp1'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('newpass/',views.newpass,name='newpass'),
    path('update_password/',views.update_password,name='update_password'),
    path('selection-status/', selection_status_view, name='selection_status_view'),
    path('status_update/<str:job_update>/<str:applied_student_id>/', views.status_update, name='status_update_page'),

    path('save-status/', views.save_status, name='save_status'),
    path('applytraining/<int:trainID>/', views.applytraining, name='applytraining'),
    path('student_signup',views.student_registration,name='student_signup'),
    path('trainer_signup',views.faculty_registration,name='faculty_signup'),
    path('submission_form/<str:course>', views.submission_form, name='submission_form'),
    path('course_submission/', views.course_submission, name="course_submission"),
    path('take-test/<str:course_id>/', views.take_test, name='take_test'),
    path('payment_page/<str:course_id>/', views.payment_page, name='payment_page'),
    path('receipt/<int:payment_id>/', views.receipt_page, name='receipt'),

    path('select-room/', views.selectroom, name='select_room'),
    path('available-rooms/', views.available_rooms, name='available_rooms'),

    path('make_payment/<int:room_id>/', views.make_payment, name='make_payment'),
    path('receipt2/<int:payment_id>/', views.receipt_page2, name='receipt2'),
    path('bus_booking/', views.bus_booking, name='bus_booking'),
    path('booking_submission/', views.booking_submission, name='booking_submission'),
    path('make_payments/', views.make_payments, name='make_payments'),
    path('bus_receipt/<int:payment_id>/', views.bus_receipt, name='bus_receipt'),
]