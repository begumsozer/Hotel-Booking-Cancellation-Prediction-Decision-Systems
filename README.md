# Hotel-Booking-Cancellation-Prediction-Decision-Systems

This project is part of the MIT No Code AI Certificate Program that I participated in. The objective of the project is to analyze hotel booking data to predict cancellations using decision systems, with a particular focus on business interpretation. By leveraging various predictive models, we aim to extract actionable insights that can help improve revenue management and customer retention strategies.

Project Overview
In this project, we work with a dataset containing detailed attributes of hotel bookings. Our primary goal is to build a decision support system that identifies high-risk bookings by analyzing:

Cancellation Rates: Understanding which bookings are likely to be canceled.

Booking Channels: Comparing online versus offline bookings.

Customer Behavior: Assessing repeated guest patterns.

Key Variables: Focusing on factors like lead time and previous cancellations.

We employed various predictive models in our analysis, including Decision Trees, Random Forests, and their pruned versions. The business interpretation approach allowed us to translate technical insights into actionable strategies, such as refining cancellation policies and optimizing pricing.

Features
Data Exploration:

Basic dataset inspection, summary statistics, and descriptive analysis.

Calculation of key percentages such as cancellation rates and repeated guest percentages.

Visualizations:

Booking channel distribution.

Cancellation distributions.

Trends in lead time, seasonal booking patterns, and market segments.

Predictive Modeling:

Implementation of Decision Trees and Random Forest models.

Pruning techniques to reduce overfitting and improve model generalization.

Evaluation of model performance using accuracy, precision, recall, and feature importance.

Business Insights:

Detailed analysis of predictive model outcomes.

Actionable recommendations for managing booking cancellations and revenue optimization.

Getting Started
Prerequisites
Python 3.x installed on your system.

Required Python libraries: pandas, matplotlib.
You can install these via pip:

bash
Copy
pip install pandas matplotlib
Running the Project
Data Preparation:
Ensure that the dataset file (Dataset-Hotel Booking Cancellation Prediction.csv) is in the specified path or modify the file path in the code accordingly.

Code Execution:
Run the provided Python script (e.g., analysis.py) to load the data, perform calculations, generate visualizations, and print key insights.

Review Results:
The script will output data summaries and display several charts to help you understand the underlying trends in the dataset.

File Structure
README.md — Project overview and instructions.

analysis.py — Python script containing data analysis, visualization, and predictive modeling code.

Dataset-Hotel Booking Cancellation Prediction.csv — The dataset used for analysis.

Presentation — Slide deck summarizing the findings and business insights.

Acknowledgements
This project was developed as part of the MIT No Code AI Certificate Program. The insights derived from the analysis help inform real-world decision systems in the hospitality industry, ultimately guiding strategies to mitigate cancellation risks and optimize operations.
