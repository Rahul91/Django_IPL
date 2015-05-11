# Django_IPL
A Python-django based Website

#Project Detail
A python-django based website, that lets user, suscribe to lastest Pepsi IPL 2015 scores and news.
The project is up-and-running i.e. deployed on Heroku.
    
    Link: http://arcane-mountain-4106.herokuapp.com/


#Logic Flow
1. User visits, the home page of the website, if he is already registered, he can then directly go to Login page, if not he can then go to Register page for registration.
2. If Registered properly, he will be routed to Registered-Successfully page. Now he can click the link present in this page to login.
3. After logging-in, user can see a notification button on top left, to which on clicking, a Javascript alert pops up that shows the latest score of IPL.
4. User can now, either choose logout or unsuscribe, depending on his choice, he will be then directed to corressponding page. Unsuscribe will be directed to home page, where as logout will direct the user to logout page.


#Features
1. Although the content of Javascript alert() is hardcoded, I  have written a script, namely ipl_result.py that scrapes the latest score from internet and outputs on screens, now this output can be feed into alert() manually. So the maintainer doesnot have to search for lastest score, instead he can just run the script and feed the output in the alert()

2. Settings.py is not hardcoded, for template paths and directories. Therefore, git clone will work fine.

#Scope/Improvments
1. alert() is hardcoded, thus it must be changed/refreshed by maintainer every day once, for the notification to be relevent.
2. As the code is deployed on heroku, after refresh, it again needs to be pushed to heroku masters.
3. The database used is sqlite3, which is not suited for bigger applicaition with high traffic, therefore it is recomended to migrate to MySql or Postgrace.

#Cloning the repository

1. Create a virtualenv, activate it and get in:

            $virtualenv <env_name>
            $source <env_name>/bin/activate
            $mkdir <env_name>

2. Clone this repo into your machine by:

            git clone https://github.com/Rahul91/Django_IPL.git

3. Install the dependencies using requirements.txt by:

            pip install requirements.txt

4. Thats, all, now you this website is up and runnig on your localhost. Just do:

            python manage.py runserver
            
#Bugs
In case of find any bug, feel free to clone it, replicate in your system, fix it and push to masters, or you drop a mail to priyrahulmishra@gmail.com
