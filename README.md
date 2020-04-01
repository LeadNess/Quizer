# Quizer

### Description
Testing system
### Installation
- ```git clone https://github.com/LeadNess/Quizer.git```
- ```cd Quizer```
- ```./build_djangoapp   #create django app and docker image```
### Usage
Run app by command:   
- ```docker run quizer```  
  
When you can connect to app in browser by following link: http://172.17.0.2:8000.
This is a test version of the program, created for demonstration purposes.   
There are 2 users in this option:
- user 'admin' with password 'admin', who belongs to group 'lecturer' and who is also a superuser (so you can enter django admin panel)
- user 'user' with password 'password', who belongs to group 'student'    

There is also 1 added subject 'Python' and 1 added test 'PZ1'.