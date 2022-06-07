# quora-duplicate-ques-checker

Creat a streamlit app to enter 2 questions and to check whether they are same or diffrent. if same then needs to merge them in single question

This project we divided in 6 main stages

==> Out of 404290 data points we use only 50000 data points bcz of having less resources to train

1) First expolatary data analysis on quora dataset like missing , duplicates, frequency of dublicates and non dublicates etc

2) Using word embedding technique Bag-of-words and count vectorizer to extract 4000 max features , train-test split and model building

3) Here we introduce some self created features to gain more accuracy , we use bag of words for questions columns, train-test split, model training
	here our main goal is to reduce the number of false positive which leads to negative impact if diffrent questions are merge

4) Here we preprocess and do some EDA on new defined features

5) Here we build randomforest classifier model, train and evaluate on test data and achieve 80.08% accuracy

6) Here we preprocess and clean the data which is passed by user and dump random forest model 

we create utils directory for all types of function such as some common , data management and for evaluating model. 
