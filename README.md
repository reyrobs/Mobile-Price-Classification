# Mobile-Price-Classification
Performating classification task on mobile price range.

# Data Exploration
![alt text](https://github.com/reyrobs/Mobile-Price-Classification/blob/main/images/box_plots.png?raw=True)

# Selecting top 5 features
Before moving to the training, we have made use of the _SelectKBest_ method from sklearn, such as to select the 5 most impactful features to predict the target class price_range. The selected classes were 'battery_power', 'mobile_wt', 'px_height', 'px_width', 'ram', such that the range of each feature can be seen in the box plots below:
![alt text](https://github.com/reyrobs/Mobile-Price-Classification/blob/main/images/data_info.png?raw=True)

# Model results
The models we have made use of are Logistic Regression and SVM, the results obtained for each model along with their confusion matrix can be seen below: <br>
Logistic Regression testing acc: 98% <br>
SVM testing acc: 96% <br>
![alt text](https://github.com/reyrobs/Mobile-Price-Classification/blob/main/images/confusion_matrix_1.png?raw=True) <br>
![alt text](https://github.com/reyrobs/Mobile-Price-Classification/blob/main/images/confusion_matrix_2.png?raw=True) <br>

# Making use of the app
In order to use the gradio app interface, please clone the repo locally and use the following command <br>
`gradio app.py` <br>
The interface can be found on the following address `http://127.0.0.1:7860`
