# Python Flask Demo

This Repo should help you to get a simple Python website setup using the Flask framework and MySQL as a database

## To-Do
- ### Preparing for the Project
  - [ ] First ensure Python is installed 
       - Run the command in Command Prompt (or any other shell) ```python --version```
       - If not installed get it from [here](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)
  - [ ] Enure MySQL Community Edition Is Installed  
       - Search For MySQL Command Line
       - If not installed get it from [here](https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.21.0.msi)
 
## Useful Stuff
- ### Commands That Will Be Used
    - #### Python Commands:
        - [ ] Installing Flask and MySQL-Connector:
           - Run the following command to install Flask and MySQL-Connector:
               - ```python -m pip install flask mysql-connector```
    - #### MySQL Commands:
        - [ ] Creating a Database and setting it up:
          - Open MySQL Command Line
          - Login Using The Password you set in setup
          - Create a database called ```demo``` using the following command:
             - ```CREATE DATABASE demo;```
          - Select that database to perform operations on it using the following command:
             - ```USE demo;```
          - Create a table called ```users``` in the database with the following command:
             - ```CREATE TABLE users (id int NOT NULL AUTO_INCREMENT, username varchar(2000), password varchar(2000), uid VARCHAR(2000), PRIMARY KEY (id));```
             - This command will create a tabe called users which contains the following columns:

                | Column | Type | Description |
                | ------ | ------ | ------ | 
                | id | INT | PRIMARY |
                | username | VARCHAR-2000 | - |
                | password | VARCHAR-2000 | - |
                | uid | VARCHAR-2000 | - |
                
## Setting Up The Test Project
 - ### Ensure steps in [To-Do](https://github.com/amitojsingh366/python-flask-demo#to-do) are completed
 - ### Run the commands in [Useful Stuff](https://github.com/amitojsingh366/python-flask-demo#useful-stuff)
 - ### Downloading the test project code
    - [ ] Download the code from this repo
       - Code can be downloaded from [here](https://github.com/amitojsingh366/python-flask-demo/archive/master.zip) or by using the button above
- ### Updating project settings
   - [ ] Editing the MySQL util file (`util.py`)
      - Change line `11` in `util.py`:
         - The feild password should be set to the password that you created while setting MySQL    server up
            - ```connection = mysql.connector.connect(host="localhost", database="demo", user="root", password="YOUR_PASSWORD_HERE")```
- ### Running The Server
   - [ ] Open the folder in which the project is located
   - [ ] Run the following command to start the server
      - ```python app.py```
   - [ ] Go to the website to see the app running
      - http://127.0.0.1:5000/ 
      - http://localhost:5000/
## Useful Links
- CSS: [W3Schools](https://www.w3schools.com/css/)
- HTML: [W3Schools](https://www.w3schools.com/html/)
- Python: [W3Schools](https://www.w3schools.com/python/)
- Flask: [Official Docs](https://flask.palletsprojects.com/en/1.1.x/)
- MySQL: [MySQLTutorial](https://www.mysqltutorial.org/basic-mysql-tutorial.aspx)