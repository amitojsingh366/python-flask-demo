# Python Flask Demo

This Repo should help you to get a simple Python website setup using the Flask framework and MySQL as a database

## To-Do
- ### Preparing for the Project
  - [x] First ensure Python is installed 
       - Run the command in Command Prompt (or any other shell) ```python --version```
       - If not installed get it from [here](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)
  - [x] Enure MySQL Community Edition Is Installed  
       - Search For MySQL Command Line
       - If not installed get it from [here](https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.21.0.msi)
  - [x] Ensure An IDE is installed (I have given popular ones below)
       - [Visual Studio Code](https://code.visualstudio.com)   <-----  the one I use
       - [Atom](https://atom.io)
       - [Pycharm](https://www.jetbrains.com/pycharm/)
       - [Jupyter Notebook](https://jupyter.org/install.html)
 
## Useful Stuff
- ### Commands That Will Be Used
    - #### Python Commands:
        - [x] Installing Flask and MySQL-Connector:
           - Run the following command to install Flask and MySQL-Connector:
               - Open your project folder in a command line and run the following command:
                   - ```python -m pip install flask mysql-connector mysql-connector-python```
    - #### MySQL Commands:
        - [x] Creating a Database and setting it up:
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
       - Extract the zip file downloaded and place the extracted folder somewhere you can remember
- ### Updating project settings
   - [ ] Editing the MySQL util file (`util.py`)
      - Change line `11` in `util.py`:
         - The feild password should be set to the password that you created while setting MySQL    server up
            - The line should look like: ```connection = mysql.connector.connect(host="localhost", database="demo", user="root", password="YOUR_PASSWORD_HERE", auth_plugin='mysql_native_password')```
- ### Running The Server
   - [ ] Open your project folder in a command line
   - [ ] Run the following command to start the server
      - Open your project folder in a command line and run the following command:
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
