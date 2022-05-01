# Item_Demand_Forecasting

![alt text](https://github.com/rasunag27/Item_demand_forecasting/blob/main/item_demand.JPG?raw=true)

Item demand forecasting is the process of making estimations over future sales demand of item over a defined period, using historical data.

### Data description

* The data consists of four data fields which are date, store, item and sales.
* The sales value is for a 5-year period starting from 2013-01-01 to 2017-12-31. 
* There are 10 stores and each store contains 10 items for which sales value is provided.

### Objective
To predict future sales of items by considering the 90 day sale.

### Methodology

* For the sales prediction, I have used Fbprophet model which is opensource and developed by Facebook. For more information check https://facebook.github.io/prophet/.
* Along with Fbprophet model, I have used traditional ML models which include Linear Regression, Decision Tree, Random Forest and XGB Regressor model.
* Data is imported and basic data analysis is studied for any null values.
* Data is explored by implementing rolling/moving average function for sales trend on items and date.
* Sales aggregation for items is done to work towards the problem objective.
* Initially, the model is implemneted for complete data to predict future sales. Trends are plotted for a particular item.
* Secondly, the data is split into train and test dataset for validation. The model is fit to trained model and predicted for test model.

### Metrics

* The performace is evaluated using r2 score as a metric.
* The r2 score is compared for all the models and for all items with actual and predicted data.
* For almost all items, the model showed that decision tree provided that max r2 score.

### Prediction

* Since Decision tree showed good performance compared to all three models, the prediction of 90 day sale for any future date is predicted by decision tree.
* The user can give input as day, week and year for the prediction. 

### Stay tuned

* The model will be deloyed via streamlit and heroku for better understanding with visualization and the link will be updated in this README file.



