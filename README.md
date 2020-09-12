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
                | password | VARCHAR-20000 | - |
                | uid | VARCHAR-2000 | - |
            
