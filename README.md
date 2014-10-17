BurstSMS API Integration
---

<br>

***Installation***
<hr>

1. First we need to install the libraries needed for this app. we will be using virtualenv to so we can isolate our python enviroment. If you don't have a virtualenv install in your machine, please check the [official documentation of virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html). 

	To create our isolated python env run the ff commands:
	
		$ cd /to/project/directory
		$ virtualenv -no-site-packages /path/to/env
		$ source /path/to/env/bin/activate
		(env) $ pip install -r requirements.txt


2. After installing the need libraries you can now run the application


		$ python manage.py runserver 
		
		
3. then go to this link [http://127.0.0.1:8000](http://127.0.0.1:8000).