import csv
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

# load Training and Testing datasets
train_file = open('database_files/dataset/Training.csv')
test_file = open('database_files/dataset/Testing - Copy.csv')

# convert into readable format from csv file
train_result = pd.read_csv(train_file)
test_result = pd.read_csv(test_file)

# Extract the Features and Target class for Training
Features_Train = train_result.drop(['prognosis'], axis=1).values
Target_Train = train_result['prognosis'].values

# Extract the Features and Target class for Testing
Features_Test = test_result.drop(['prognosis'], axis=1).values
Target_Test = test_result['prognosis'].values

gnb = GaussianNB()

gnb.fit(Features_Train, Target_Train)
################################################
# all the diseases that model can predict(41)
tags = np.unique(Target_Train)

# data to check for prediction
Features_Predict = Features_Test[:2]

# predicting with probability for each disease
predicts = gnb.predict_proba(Features_Predict)

# create dictionary with key as disease and probability as value {'disease': 0.5}
# predict_proba gives nested array,
# when single row of data provided, we have to access the internal array
pred_dict = dict(zip(tags, predicts[0]))
# sort dictionary based on probability
dicts = sorted(pred_dict.items(), key=lambda x: x[1], reverse=True)

# print only top 3 disease with highest probability
for i in range(3):
    if dicts[i][1] >= 0.30:
        print(dicts[i][0], ' --> Accuracy: ', round(dicts[i][1]*100), '%')
