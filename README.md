# project-course-3-udacity
# Overview

Build a Github repository from scatch and create a scaffolding in performing both Continuous Integration and Continuous Delevery.

## Project Plan

* A link to a Trello board for the project: https://trello.com/b/rDv9z2TX/software-development-project
* A link to a spreadsheet that includes the original and final project plan: https://docs.google.com/spreadsheets/d/1CB27icAbr3qya7oZXqTplgqL7MNvgXdP/edit?usp=sharing&ouid=106957848057168331648&rtpof=true&sd=true

## Instructions

* Architectural Diagram
  
  ![image](https://github.com/user-attachments/assets/ea944301-d8c3-4dcc-9f75-620915093524)

* Project cloned into Azure Cloud Shell
  
  ![image](https://github.com/user-attachments/assets/f96484b0-ea4c-4501-b3e7-1ceac780eb54)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
  
  ![image](https://github.com/user-attachments/assets/7ddf5e72-8b0b-4b0d-8645-c5ef7f317b03)

* Output of a test run

  ![image](https://github.com/user-attachments/assets/e97a3d52-3c01-40a8-99a6-3939b8604016)

  ![image](https://github.com/user-attachments/assets/ef8331cd-90a2-4d09-98c1-26c77e4ec798)

* Running Azure App Service from Azure Pipelines automatic deployment and successful deploy of the project in Azure Pipelines. 
  
  ![image](https://github.com/user-attachments/assets/9466e4fa-fa61-4fbf-8485-3452fa5cb8c7)

* Successful prediction from deployed flask app in Azure Cloud Shell.

  ![make_prediction](https://github.com/user-attachments/assets/2a33a345-a228-4c52-b603-5ad7b290b058)
  
The output should look similar to this:
  ![image](https://github.com/user-attachments/assets/6068e1c8-646b-465f-8c3c-fa5445e062c8)

```bash
(.udacity-devops) odl_user [ ~/project-course-3-udacity ]$ ./make_predict_azure_app.sh 
Port: 443
{"prediction":[2.431574790057212]}
```

* Output of streamed log files from deployed application

  ![stream log part 1](https://github.com/user-attachments/assets/ba553bad-0df0-410e-b8e1-7105b24a3573)
  ![stream log part 2](https://github.com/user-attachments/assets/5a1d2db8-7c8a-46e9-8693-e7ff1a0208e2)


## Enhancements

To improve the project in the future, we can approve some key below:
* Use Containerization
* Implement Microservices
* Automated Testing
* Caching
* Load Balancing
* Security Best Practices
* Vulnerability Scanning

## Demo 

Link demo: N/A

![example workflow](https://github.com/trungthangdk/course-3-udacity/actions/workflows/main_myapp-thangnt16.yml/badge.svg)

