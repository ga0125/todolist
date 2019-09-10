# todolist
Hey bro! This is a simple web app ToDo List using Django. Here we go!

#Application accesses

#h2User Django-admin

**user:** admin | password: admin

#h2Pages

**Web application:** [My Tasks](http://127.0.0.1:8000)
**Admin Page:** [My Tasks - Admin](http://127.0.0.1:8000/admin)
**APIs:** [My Tasks - API](http://127.0.0.1:8000/api)

#Archicteture

#h3•	Frontend

**Used Technologies -** For this project I’ve used HTML 5 (DHTML), CSS3, JS and bootstrap 4 framework. 

**Application’s description -** Please check below the My Task’s description to make the usability clearer for the end user:

#h2•	Adding a Task:
	**o	Add a Tile (obligatory field) -** You can insert any char value with till 80 characters;

	**o	Add a Description (obligatory field) -** You can add any char value with till 200 characters;
	
	**o	Choose a Deadline -** On the “Datetimefield” you can choose a deadline for this task to be inserted. If you don’t set a deadline, the system will be inserting the current day by default;
	*PS: You can press “enter” or click on “+ Task” to add you task.*

#h2•	Controlling a Task:
	**o	Task line added -** Every task, after added on the system, will be showed for the end user like a single line showing only the task Title and some action buttons;

	**o	Description and deadline task –** You can find the “Description button ( ˅ )” on the right div side, when you click the description and deadline task will be  appear on the screen;

	**o	Exclude a task –** Now, if you need exclude a task, you can find a “trash icon” besides of the “Description button”. So, be careful, because every task excluded will not be recovered!

	**o	Complete a Task –** When you finish your task (congrats bro!) you just need check the checkbox button and finish it. Off course, every task checked as completed you cannot come back, so make sure that you finish that task at all hehehe;




#h3•	Backend

**Used Technologies -** For the backend I’ve used Python, Django and Django rest framework.

**DB Structure -** check below the DB structure adopted for this app:


|Id| This value is generated automatically by the DB| 
|Title|Char value with till 80 characters|
|Description| Char value with till 200 characters|
|Deadline| Date value for the deadline date (I got this value using input type date)|
|Complete| Boolean value that I use for the checkbox|
|Completed_at| When the task is checked as complete this field will be inserted with the current datetime|

**APIs –** The APIs of this web application was designed using Django rest framework. To have access to these APIs, firstly, you need log in as ‘admin’ on the page [Admin](http://127.0.0.1:8000/admin). After logged, you can access the page [API](http://127.0.0.1:8000/api) and check/test/filter the APIs (Feel free to use it bro!).
*PS: I’ve chose the user permission authentication method to use the APIs for this test.*

#Conclusion

I hope you enjoy the My Tasks, and regardless of the completion of this test, I appreciate the opportunity where I could learn even more.
