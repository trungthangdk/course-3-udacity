![example workflow](https://github.com/trungthangdk/course-3-udacity/actions/workflows/pythonapp.yml/badge.svg)
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
![image](https://github.com/user-attachments/assets/e5d20a87-971f-4595-bf04-dc5593cf9f70)

* Output of a test run

  ![image](https://github.com/user-attachments/assets/3a7dca9a-569c-4567-914b-cd48f00611ee)
![image](https://github.com/user-attachments/assets/a2f9ac0c-6428-482d-add6-c65109131241)


* Running Azure App Service from Azure Pipelines automatic deployment and successful deploy of the project in Azure Pipelines. 
  
  <img width="1393" alt="image" src="https://github.com/user-attachments/assets/e594ed8e-c597-47c8-ab1e-bb713892b455">

* Successful prediction from deployed flask app in Azure Cloud Shell.

  ![image](https://github.com/user-attachments/assets/c2cdb3d2-9e73-4dac-b86b-e80835d6f863)

  
The output should look similar to this:
  ![image](https://github.com/user-attachments/assets/ca16a8db-5fa7-4bdf-988f-9555d7e8c9d2)


```bash
(.udacity-devops) odl_user [ ~/project-course-3-udacity ]$ ./make_predict_azure_app.sh 
Port: 443
{"prediction":[2.431574790057212]}
```

* Output of streamed log files from deployed application

![image](https://github.com/user-attachments/assets/c9d4cd8b-1d56-4494-98e9-0946a1ba202b)
![image](https://github.com/user-attachments/assets/18a9c53d-bb60-45e8-82b2-8eae159c92e7)
![image](https://github.com/user-attachments/assets/73927a71-0c9d-4a33-952b-45139ea62701)
![image](https://github.com/user-attachments/assets/157bb5fd-040c-4e09-b544-6dac67739ec8)
![image](https://github.com/user-attachments/assets/08a432bf-7586-4b90-a94b-ab89a26dc946)
![image](https://github.com/user-attachments/assets/7ba67b1b-0389-4ebf-a16b-f3156d5734be)
![image](https://github.com/user-attachments/assets/97e4fb4a-9797-4578-b85e-561bc6a9bb39)

## Enhancements

To improve the project in the future, we can approve some key below:
* Create UI
* Use Containerization
* Implement more function

## Demo 

Link demo: https://youtu.be/1Y4KSmwN-5E

![image](https://github.com/user-attachments/assets/feb20538-2443-4b28-ab33-70315b9a6cdd)


