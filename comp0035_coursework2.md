# Coursework 2

## Requirements definition and analysis
The term 'requirements' is used in the broader sense, user stories and/or use cases may be used.
### Requirements identification methods

In order to elicit requirements i will be using these methods:

•	Brainstorming - this method is suitable as for individual work as for group works. It is simply a way of coming up with ideas by writing on paper everything that the person/people can come up with. This method is very suitable for requirements as it provides with a lot of different ideas and might even make the website more diverse.
•	Survey/Questionnaire of the targeted group - this is a great method as it provides feedback from already created similar websites. This is a better approach for people who have not created websites before. I would say it is more safe way of collecting data and it will be used to compare ideas that are created using brainstroming.
•	Compare my webapp with other applications for data representation - this method does not involve any direct feedback. We are just gonna look at running websites and compare visually what aspects we might consider adding to our website. 


### Requirement specification method

For this web application I will be using User Stories as requirements specification method.

•	As a user, I would like to be able to create an account

  Acceptance criteria:
    1. User inputs available email and password.
    2. User must repeat password twice
    3. Additional confirmation is required via email

  
•	As a user, I would like to be able to download selected data in a specified format.

  Acceptance criteria:
    1. Selection of different format files should be available


•	As a website user, I want to have search functionality on all pages.
  
  Acceptance criteria:
    1. Search box should accept any value
    2. Search results should show 5 areas per page
    3. System should respond to all requests within 3 seconds of receiving a request

•	As a website user, I need to have option of filtering data based on year of vehicle licensing.
  
  Acceptance criteria:
    1. Filter would change the graph in 3 seconds withing receiving a request.
    2. Filter would be applied in case of download of the data.

•	As a website user, i would like the website to remember my login credentials and keep me logged in. 
  
  Acceptance criteria:
    1. Stay logged in after restarting computer
    2. Website must log out user after them changing email/password
    3. Ask whether user would like to stay logged in


•	As a website user, i would like to have option of changing password/email.
  
  Acceptance criteria:
    1. News of change of password would be emailed to the associated email. 
    2. New password would be created via link that was sent to the associated email for better protection.
    3. In case of changing email an additional confirmation would be sent to the previous email.


•	As a website user, i would like for the website to remember all the setting I have used and all the data i have filtered.
  
  Acceptance criteria:
    1. After logging in, all the progress, filters, selected parts of data from the previous work should be saved.


•	As a website user, I would like to have an option of choosing different charts/graphs for specified data representation
  
  Acceptance criteria:
    1. Available options: Bar Chart, Pie Chart, Scatter Plot, Gantt Chart. 
    2. After chosing one of the available options system would refresh the page within 3 seconds

•	As a website admin, I would like to be able to ban people from using my website 
  
  Acceptance criteria:
    1. I can temporarily disable their access
    2. It is possible to ban their ip

•	As a website user, I would like to be able to comment under different graphs/data structures.
  
  Acceptance criteria:
    1. There would be an option of replying to comments.
    2. Reporting comments.
    3. Removing own comments.
    4. Liking/Disliking other peoples comments.
    
•	As a website user, I would like the website to be safe for reading.
  
  Acceptance criteria:
    1. Website should have word filtering software which would not allow users to comment bad languaguage words.
    2. Ability to report people. 
    
•	As a website user, I would like to have an option of writing an email to support just in case.
  
  Acceptance criteria:
    1. Response within 3 working days

•	As a website user, I would like to be able to access website from my phone.
  
  Acceptance criteria:
    1. It should run on OS version higher than 9.3.6 ios or 9 android version (also known as andoroid pie)
    2. Website should be readjusted to different models of phones or tablets.

•	As a website user, I would like to have access to data sets only after creating an account, therefore, supporting creator

  Acceptance criteria:
    1. Access to data charts after setting up an account

### Prioritisation method

I will be using classical prioritisation method using numbers. This will avoid all requirements becoming 'high priority'. I have created a file that will represent my requirements. They are put in a way from high priority to lowest priority (decreasing priority). 

([requirements](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/requirementspriority.xlsx))

In the file there are 13 requirements in total. I have listed them as I would like my website to be build. I have put create an account as the most important requirement because I would only provide data after registering on the website. Afterwards, all these accounts could be used for mail marketing etc. All other requirements do not need any specific explanation as their position is simple to understand. 

Using requirements I have produced use case diagram which should explain the flow of website better:

([user diagram](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/UserDiagram.jpg))

## Design

### Structure and flow of the interface

Wireframes reference:

Signup page:
([Signup](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/Wireframes/Signup.png))

Login page:
([Login](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/Wireframes/Login.png))

Main page:
([Main](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/Wireframes/MainPage.png))

Data page:
([Data](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/Wireframes/Data.png))

Password reset request page:
([reset request](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/Wireframes/PasswordResetURL.png))

Password reset page:
([Reset](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/Wireframes/PasswordReset.png))

Logout page:
([Logout](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/Wireframes/Logout.png))

For better application representation I have created application architecture following this model:

([flaskmodel.png](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/flaskmodel.png))

Here is a list of routes, referenced wireframes and the controller functions:

([routes.xlsx](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/routes.xlsx))

When user wants to access something the model works in a loop. User uses controller to manipulate model. This in sequence, upadtes view of the website and user is able to see new representation of the data.

### Relational database design

For the relational database design creation I have used Lucid Charts website:

([erd.png](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/erd.png))

### Application structure

Application structure is represented in a class diagram:

([uml.png](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/uml.png))

## Testing
### Choice of unit testing library

I have chosen to use pytest as it is much more powerful tool for testing and is widely used in the software development industry. 

### Tests
Tests are in a seperate directory:

([user_test.py](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/test/test_user.py))

### Test results

Results of testing:
([testResults.png](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/test/testResults.png))

## References

[figma - website used for wireframes](https://www.figma.com/?fuid=) 

[lucidcharts - website used for diagrams](https://lucid.co/) 

[guidelines for uml diagram](https://www.lucidchart.com/pages/uml-class-diagram/#section_3) 



