# project-course-3-udacity
# Overview

Build a Github repository from scatch and create a scaffolding in performing both Continuous Integration and Continuous Delevery .

## Project Plan

* A link to a Trello board for the project: https://trello.com/b/pJFisPY0/software-development-project
* A link to a spreadsheet that includes the original and final project plan: https://docs.google.com/spreadsheets/d/1QSOcjyTG86EBITK6XWIugyxb4SanNuOdba1365I_SVo/edit?usp=sharing

## Instructions

* Architectural Diagram
  
  ![image](https://github.com/user-attachments/assets/7b17e92b-c2b4-4344-a51e-5d2418b814f1)

* Project cloned into Azure Cloud Shell
  
  <img width="1393" alt="image" src="https://github.com/user-attachments/assets/0f09b503-70e3-40b9-a25f-34720a14b504">


* Passing tests that are displayed after running the `make all` command from the `Makefile`
  
 <img width="1395" alt="image" src="https://github.com/user-attachments/assets/3275288f-4346-4793-b73b-25c23e26540a">

* Output of a test run
<img width="1393" alt="image" src="https://github.com/user-attachments/assets/ac8ce327-0b01-42e0-8658-b4f9617b636e">


* Running Azure App Service from Azure Pipelines automatic deployment and successful deploy of the project in Azure Pipelines. 
  
  ![image](https://github.com/user-attachments/assets/e4afb01c-344d-4255-add1-07b742f8df45)


* Successful prediction from deployed flask app in Azure Cloud Shell.

<img width="1394" alt="image" src="https://github.com/user-attachments/assets/b7e7b7bb-02a2-473c-a24a-d9b423e243d1">

  
The output should look similar to this:
<img width="1393" alt="image" src="https://github.com/user-attachments/assets/79c67e42-ca5c-479b-93d8-001cf3203bca">


```bash
odl_user [ ~/course-3-udacity ]$ ./make_predict_azure_app.sh
Port: 443
{"prediction - thangnt16 - test":[2.431574790057212]}
```

* Output of streamed log files from deployed application
![image](https://github.com/user-attachments/assets/e1bcf2c3-c2fb-4e65-bf32-373241211210)
![image](https://github.com/user-attachments/assets/f2fc204d-fbbe-4453-a194-0f69c163526c)
![image](https://github.com/user-attachments/assets/9933af7c-f845-499a-afda-b47c683c718c)
![image](https://github.com/user-attachments/assets/b6776847-5480-4c73-8c9e-11fe5268c211)

## Enhancements

To improve the project in the future, we can approve some key below:
* Create UI
* Use Containerization
* Implement more function

## Demo 


![example workflow](https://github.com/trungthangdk/course-3-udacity/actions/workflows/pythonapp.yml/badge.svg)




