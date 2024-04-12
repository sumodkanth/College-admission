cd# College_Job_Portal

# overview

This project is a Python Django-based web application for managing a college job portal. The portal allows students to explore job vacancies, apply for jobs, view training programs, and access various study materials. Faculty members, designated as administrators, have the authority to manage students, faculty, courses, departments, jobs, placed students, and training programs.

# Getting Started

Follow these steps to set up and run the project on your local machine: <br>

# System Requirements

Ensure that your system meets the following requirements to successfully set up and run the College Job Portal:<br>

# Software Requirements

Python: Version 3.6 or higher<br>
Django: Version 3.0 or higher<br>
Database: SQLite (default for Django)<br>

# Installation

Clone this repository to your local machine<br>
#### git clone https://github.com/ryban94/job-Portal.git<br>

Navigate to the project directory.<br>
#### cd CMS

Activate the virtual Environment.<br>
#### myenv\scripts\activate<br>

Install the required dependencies.<br>
#### pip install -r requirements.txt

Apply initial migrations to set up the database:<br>

#### python manage.py makemigrations
#### python manage.py migrate<br>

Configure email settings in the settings.py file to enable the "Forgot Password" feature.<br>

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'<br>
EMAIL_HOST = 'your_smtp_server'<br>
EMAIL_PORT = 587<br>
EMAIL_USE_TLS = True<br>
EMAIL_HOST_USER = 'your_email@example.com'<br>
EMAIL_HOST_PASSWORD = 'your_email_password'<br>

Run the server.<br>

#### python manage.py runserver<br>
###### The server will be running at http://127.0.0.1:8000/.

# Admin Credentials

Username: 4 <br>
Password: 9876543210 <br>

# User Authentication

Only administrators can create accounts for students and faculty.<br>
Users can log in using their user ID and mobile number.<br>
Users can reset their password using the "Forgot Password" feature, which involves receiving an OTP via email.<br>

# Admin Authority

Admin faculty members have the authority to add, modify, and delete students, faculty, courses, departments, jobs, placed students, and training programs.<br>

# Navigation
    Home Page Navbar:<br>

        Home<br>
        Recruiters<br>
        Contact Us<br>
        Gallary<br>
        Help<br>
        Job Vacancy List<br>
        Training Program List<br>
    
    Home Page Body:<br><br>

        View Jobs List<br>
        Placed Student List<br>
        Study Programs<br>
        Aptitude, etc.<br>
        View Training Programs<br>

# Job Application Process
    Students can apply for jobs.<br>
    Students can upload their resumes during the application.<br>
    Once a student applies for a job, they cannot apply for the same job again.<br>
    Faculty can view the resumes of students who have applied under their respective companies.<br>
    Feel free to explore the features and functionalities of the College Job Portal! If you have any questions or issues, please refer to the help section or contact us.<br>
