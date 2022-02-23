
**General Notes**<br/><br/>
As "Django Application Development with SQL and Databases" EDX-IBM course final project, an `onlinecourse` app is provided in this repo.<br/>

The project has been developed locally on VSCode IDE, and deployed to IBM Cloud Foundry:<br/>

https://pettib01.us-south.cf.appdomain.cloud/onlinecourse/<br/>

where you can see it working (a bit slow I should say).<br/>

Three courses with lessons and its  non-exclusive multiple choice exams have been created, in addition some user have been signed up as instructor or as student.<br/>

A layout.html file is added with headings and nav bar, common to all templates, with context data just to change the "home link".<br/>
A custom_tags.py file is added in order to allow the use of dictionaries with variables into the templates.<br/>

Feel free to signup as site user, and enroll yourself in any course. You can take an exam and see the results. Or you can use already existing accounts like the following students:<br/>
user: knows_nothing     password: ignorant77<br/>
user: knows_little      password: beginner77<br/>
user: knows_enough      password: intermediate77<br/>
user: knows_alot        password: advanced77<br/>

Or login at admin page as instructor with teh following credentials, which allows you to create new courses with lessons, questions and choices.<br/>
user: john_django       password: master77<br/>
user: dr_dolittle       password: animals77<br/>

Code has several "print" (to terminal) instructions just for debugging purposes.<br/><br/>

**ER Diagram:**<br/>
An ER diagram design is provided for reference.<br/>

![Onlinecourse ER Diagram](https://github.com/ibm-developer-skills-network/final-cloud-app-with-database/blob/master/static/media/course_images/onlinecourse_app_er.png)
