Cricket Analytics Projects
This repository contains two Python-based cricket analytics projects:
1.	IPL Match Data Web Scraping 
2.	Asia Cup Match Outcome Prediction using Machine Learning

   
Project 1: IPL Match Data Web Scraping
Description
This project collects IPL match statistics from the HowStat cricket website using web scraping techniques. The scraped data is cleaned, transformed, and exported into a CSV file for further analysis.
Features
•	Extracts IPL match data from a live website 
•	Parses HTML tables using BeautifulSoup 
•	Cleans and structures the data using Pandas 
•	Exports the final dataset to CSV format 
•	Performs basic exploratory analysis on recent matches 
Technologies Used
•	Python 
•	Requests 
•	BeautifulSoup (bs4) 
•	Pandas 
Dataset Output
match_data.csv
Contains IPL match information such as:
•	Team Names 
•	Opponent Teams 
•	Venue 
•	Match Date 
•	Winner 
•	Winning Margin



Project 2: Asia Cup Match Outcome Prediction

Description
This project builds a Machine Learning model to predict Asia Cup cricket match outcomes using historical match statistics and team performance data.

The project includes:
•	Data Cleaning 
•	Feature Engineering 
•	Label Encoding 
•	Feature Scaling 
•	Model Training 
•	Performance Evaluation

Features
•	Handles missing values 
•	Encodes categorical variables 
•	Scales numerical features 
•	Trains a Logistic Regression model 
•	Evaluates model performance using classification metrics 

Technologies Used
•	Python 
•	Pandas 
•	NumPy 
•	Matplotlib 
•	Seaborn 
•	Scikit-learn 

Dataset
model_dataset.csv

Contains historical Asia Cup match statistics including:
•	Team 
•	Opponent 
•	Toss Result 
•	Match Format 
•	Run Scored 
•	Wickets Taken 
•	Run Rate 
•	Batting Statistics 
•	Bowling Statistics 
•	Match Result

Evaluation Metrics
The model is evaluated using:
•	Accuracy Score 
•	F1 Score 
•	Confusion Matrix 

Challenges Faced
Web Scraping Project
•	Identifying the correct HTML table from the webpage 
•	Cleaning inconsistent scraped data 
•	Converting raw HTML content into structured datasets 

Machine Learning Project
•	Handling missing values 
•	Encoding categorical features 
•	Selecting relevant features for prediction 
•	Improving model performance and evaluation

