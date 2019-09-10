# My Tasks
Hey bro! This is a simple web app ToDo List using Django. Here we go!

# Application accesses

## User Django-admin

**user:** admin | password: admin

## Pages

**Web application:** [My Tasks](http://127.0.0.1:8000)
**Admin Page:** [My Tasks - Admin](http://127.0.0.1:8000/admin)
**APIs:** [My Tasks - API](http://127.0.0.1:8000/api)

# Archicteture

### •	Frontend

**Used Technologies -** For this project I’ve used HTML 5 (DHTML), CSS3, JS and bootstrap 4 framework. 

**Application’s description -** Please check below the My Task’s description to make the usability clearer for the end user:

## •	Adding a Task:

	o Add a Tile (obligatory field) -** You can insert any char value with till 80 characters;

	o Add a Description (obligatory field) -** You can add any char value with till 200 characters;
	
	o Choose a Deadline -** On the “Datetimefield” you can choose a deadline for this task to be inserted. If you don’t set a 	  deadline, the system will be inserting the current day by default;
	
	PS: You can press “enter” or click on “+ Task” to add you task.

## • Controlling a Task:

	- Task line added - Every task, after added on the system, will be showed for the end user like a single line showing only the task Title and some action buttons;

	- Description and deadline task – You can find the “Description button ( ˅ )” on the right div side, when you click the description and deadline task will be  appear on the screen;
	- Exclude a task – Now, if you need exclude a task, you can find a “trash icon” besides of the “Description button”. So, be careful, because every task excluded will not be recovered!
	- Complete a Task – When you finish your task (congrats bro!) you just need check the checkbox button and finish it. Off course, every task checked as completed you cannot come back, so make sure that you finish that task at all hehehe;

### •	Backend

**Used Technologies -** For the backend I’ve used Python, Django and Django rest framework.

**DB Structure -** check below the DB structure adopted for this app:

Fields | Description
--------- | ---------
id | This value is generated automatically by the DB
title | Char value with till 80 characters
description |  Char value with till 200 characters
deadline | Date value for the deadline date (I got this value using input type date)
complete | Boolean value that I use for the checkbox
complete_at | When the task is checked as complete this field will be inserted with the current datetime

**APIs –** The APIs of this web application was designed using Django rest framework. To have access to these APIs, firstly, you need log in as ‘admin’ on the page [Admin](http://127.0.0.1:8000/admin). After logged, you can access the page [API](http://127.0.0.1:8000/api) and check/test/filter the APIs (Feel free to use it bro!).
*PS: I’ve chose the user permission authentication method to use the APIs for this test.*

# Conclusion

I hope you enjoy the My Tasks, and regardless of the completion of this test, I appreciate the opportunity where I could learn even more.
