# Artificial Intelligence Work Prompt


***Contents of EDM.py***

Contains the basic exploratory data analysis for all the data. Makes use of pandas to sort read in the excel file and understand the data. I have first seperated the data by
Years and then analyzed the menu orders for each year. The MatPlot library was used to plot the menu items that each year ordered. This helps us see which menu item was the
most popular for each year. The same thing is done for each University through which we can see what menu item sells the most for each university. Images of bar plots are
attached in the repository.



***Contents of model.py***

Attempts to use sklearn to create a machine learning model. The model used is Random Forest Classifier. This reads in the excel file and sets the target and feature variables. The model is then trained for each variable and in the end returns a prediction for the target (dependent) variable. The prediction is printed out onto the terminal
