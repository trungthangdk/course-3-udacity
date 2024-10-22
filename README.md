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
  
  ![image](https://github.com/user-attachments/assets/78f92297-a296-4069-9fce-0371d1753ea1)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
  
 ![image](https://github.com/user-attachments/assets/739368ab-397f-4f72-bb79-43bd5a4ea78f)
* Output of a test run
![image](https://github.com/user-attachments/assets/e5d20a87-971f-4595-bf04-dc5593cf9f70)

* Running Azure App Service from Azure Pipelines automatic deployment and successful deploy of the project in Azure Pipelines. 
  
  ![image](https://github.com/user-attachments/assets/e4afb01c-344d-4255-add1-07b742f8df45)


* Successful prediction from deployed flask app in Azure Cloud Shell.

 ![image](https://github.com/user-attachments/assets/17aa0952-5ed0-4f11-ba68-271c79e30943)

  
The output should look similar to this:
  ![image](https://github.com/user-attachments/assets/ca16a8db-5fa7-4bdf-988f-9555d7e8c9d2)


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

Demo Azure cloud shell: https://youtu.be/TEigyXAMWi8
Demo Github action: https://youtu.be/mle2cOn0uOI
Demo Continuous Delivery: https://youtu.be/QO-j-4cszAc

![example workflow](https://github.com/trungthangdk/course-3-udacity/actions/workflows/pythonapp.yml/badge.svg)
![image](https://github.com/user-attachments/assets/fdb0f266-f514-4a02-bc44-1b0a4e3fc698)



