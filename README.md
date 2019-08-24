# About this app

	It is a website on the course "Coarse Grained POS-Tagging (Computational Linguistics)". Python flask framework is used to make this website with some backened work using sqlite and ajax.

# Run Application
```
1. To run this application, you need to install flask, sqlalchemy, pytest.Go to Command Terminal:
	$ pip3 install flask
	$ pip3 install flask_sqlalchemy
	$ pip3 install pytest
2. Now run run.py file on your Command Terminal 
	$ python3 run.py
3. Right Click on link shown on terminal and open it in browser.
```
# Folder Structure
```	
1. run.py 							#imports app,db from exp7 and run app.
2. exp7
	1. __init__.py 					#imports flask,routes , contain app, db.
	2. routes.py 					#contains all routes
	3. models.py 					#contains database classes
	4. templates 					#contains all html files
		index.html 					#contains layout part of website
		other files contain the main block containing part as indicated by their name.
	5. static
		1.images  
		2.css
			style.css 				#contains css part of all html files
			Css libraries
		3.js
			custom.js 				#contain js part of all html files
			JS libraries
	6. exp.db 						#database file contains all sentences and options and correct answers of experiment.
3. Documentation.py 				#contains description of all functions
4. README.md 						#about how to run app and file structure
5. test_link.py 					#checks whether all links are working
6. appTest.py 						#runs test cases of experiments
```