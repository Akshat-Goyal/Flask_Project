
# Run Application
```
1. To run this application, you need to install flask, sqlalchemy.Go to Command Terminal:
    $ pip3 install flask
    $ pip3 install flask_sqlalchemy
2. Now run run.py file on your Command Terminal 
    $ python3 run.py
3. Right Click on link shown on terminal and open it in browser.
```
# Folder Structure
```	
1. run.py 				            #import app,db from exp7 and run app
2. exp7
    1. __init__.py 	 	            #import flask , contain app, db, all routes
    2. experiment.py 	            #contain database classes
    3. templates			        #contain all html files
        index.html 			        #contain layout part of website
        other files contain the main block containing part as indicated by their name.
    4. static
        1.images                      
        2.css
            style.css               #contain css part of all html files
            some downloaded css files
        3.js
            custom.js               #contain js part of all html files
            some downloaded js files
```