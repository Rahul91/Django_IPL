# Django_IPL
A Python-django based Website

#Project Detail
A python-django based website, that lets user, suscribe to lastest Pepsi IPL 2015 scores and news.
The project is up-and-running i.e. deployed on Heroku.
Notification is the name of Project and signups is the App.
    
    Link: http://arcane-mountain-4106.herokuapp.com/


#Logic Flow
1. User visits, the home page of the website, if he is already registered, he can then directly go to Login page, if not he can then go to Register page for registration.
2. If Registered properly, he will be routed to Registered-Successfully page. Now he can click the link present in this page to login.
3. Thats it!!!. User will now, recieve notification on his desktop.
4. User can now, either choose logout or unsuscribe, depending on his choice, he will be then directed to corressponding page. Unsuscribe will be directed to home page, where as logout will direct the user to logout page.

#Technologies Used

   1. Python(Core)
   2. Django(Framework)
   3. Javascript(The Programming backbone for HMTL)
   4. HTML(becasue, its needed!!!)
   5. AJAX(For Server-side Communication)
   6. CSS(For Styling)
   7. XML(Data)
   8. Yahoo API
   9. Sqlite3(Database)
  
#Cloning the repository

1. Create a virtualenv, activate it and get in:

            $virtualenv <env_name>
            $source <env_name>/bin/activate
            $cd <env_name>

2. Clone this repo into your machine by:

            git clone https://github.com/Rahul91/Django_IPL.git

3. Install the dependencies using requirements.txt by:

            pip install requirements.txt

4. Thats, all, now you this website is up and runnig on your localhost. Just do:

            python manage.py runserver
            
#Bugs
In case of find any bug, feel free to clone it, replicate in your system, fix it and push to masters, or you drop a mail to priyrahulmishra@gmail.com
