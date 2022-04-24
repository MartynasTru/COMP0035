# Coursework 1

## Technical information
### Repository URL

[GitHub repository](https://github.com/ucl-comp0035/coursework-1-MartynasTru)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!


## Selection of project methodology

For this particular data set, I believe that CRISP-DM is the most suitable method to use.

### Selection criteria and justification of selection

I believe that the data science method is much more viable and doable for an individual type of project. I have chosen CRIPSP-DM as the data science method for my project for these particular reasons. First of all, business understanding and data understanding are interconnected which means it is possible to go back and forth between these stages of the project development. Moreover, data preparation and modelling are linked as well which means the methodology is extremely flexible. In addition to this, there is a stage of Evaluation that allows checking business understanding with the current product. In case of some difference, it is possible to go back to business understanding and modify the project. In my opinion, this is an ideal method to use for my particular set of data and individual projects in general. 

## Definition of the business need

Companies should build more parking spaces in areas with the highest growth of car's licensing.

### Problem definition

Every year there is an increase of drivers in the United Kingdom who struggle to find a parking spot around some areas. This is problematic as it slows down traffic, wastes time and money. All kinds of people are affected by it: businessmen, engineers, policemen, ambulances etc. Moreover, being late to a meeting, conference, gathering might strongly affect peoples' life, or the police being late a couple of seconds may not be able to help someone. Shortage of places occurs during peak hours or generally every year there is a need to build more parking spots for people to fit in the city.

### Target audience

The target audience of my project is Data Analysts working in the UK and can be found here:
[Persona](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/persona/111.PNG)

### Questions to be answered using the dataset

How many cars are licensed every year in GreatBritain?
How many cars are licensed in different areas?
What are has the most cars licensed a year compared to other areas.

## Data preparation and exploration
### Data preparation

[data_preparation.py](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/data_preparation.py)

### Prepared data set

[DataPointsWithAreas.xlsx](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/DataPointsWithAreas.xlsx)
[PreparedDataWithAreas.csv](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/PreparedDataWithAreas.csv)

### Data exploration

[data_exploration.py](https://github.com/ucl-comp0035/coursework-1-MartynasTru/blob/master/data_exploration.py)

While data exploring I was following 'guidance'. However, I have quickly discovered that most of them are not suitable for my type of data. I have time in Quarters which are not recognised using regular pandas syntax and Vehicles numbers that were licensed throughout time.

I have tried plotting other kinds of plots like 'hist' or 'bar' or 'box'. However, I have concluded that a classical line plot best describes the growth of car licenses and the future need for storage of the vehicles. I believe that growth in car licenses will continue to be positive based on the previous 30 years (68 measured points).

## Weekly progress reports

What I did in the last week:

What I plan to do in the next week:

Issues blocking my progress (state ‘None’ if there are no issues):


### Report 1

I have set up my GitHub Environment. Moreover, I have setup up my python in Visual Basic Studio as well as PyCharm, however, I prefer VSCode. Therefore, I'll continue working with VSCode. In addition to this, I went through the material for the coursework and decided on a method that I'm gonna use. 

I'm planning to start working on my coursework 1 more. Moreover, I ll try to go ahead in this module, so that I can spend more time doing Project 1.

Had some issues with repository, however, all of them are solved by this time. 

### Report 2

I have started writing a list of people and their characters/preferences that will use my provided data. I have attended the lecture and got crucial information on how to write a problem statement.

I am planning to furtherly work on the materials that will be provided in the next week.

None

### Report 3

I have looked into data exploration using pandas. Went through the weeks lessons and started exploring data for my coursework 1.

I am planning to continue with data exploration and preparation for the coursework 1.

I was very sick this week, that is why I am late in submission of this progress report.

### Report 4

I have worked on gathering elicit requirements for my data. I have spent some time exploring data and will finish my coursework from 06-07 of November. 

I am planning on polishing my coursework 1 and submitting it on the weekend 06-07 of November.

None

## References
1. [Data Exploration](https://moodle.ucl.ac.uk/pluginfile.php/4320438/mod_resource/content/2/ht_data_exploration.pdf) 
2. [Data Preparation](https://moodle.ucl.ac.uk/pluginfile.php/4320406/mod_resource/content/1/ht_data_preparation.pdf)