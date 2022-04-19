# Item_Demand_Forecasting

![alt text](https://github.com/rasunag27/Item_demand_forecasting/blob/main/item_demand.JPG?raw=true)

Item demand forecasting is the process of making estimations over future sales demand of item over a defined period, using historical data.

### Data description

* The data consists of four data fields which are date, store, item and sales.
* The sales value is for a 5-year period starting from 2013-01-01 to 2017-12-31. 
* There are 10 stores and each store contains 10 items for which sales value is provided.

### Objective
To predict 3-month sales of each item by considering the aggregation of stores.

### Methodology

* For the sales prediction, I have used Fbprophet model which is opensource and developed by Facebook. For more information check https://facebook.github.io/prophet/
* Data is imported and basic data analysis is studied for any null values.
* Data is explored by implementing rolling/moving average function for sales trend on items and date.
* Sales aggregation for items is done to work towards the problem objective.
* Initially, the model is implemneted for complete data to predict future sales. Trends are plotted for a particular item.
* Secondly, the data is split into train and test dataset for validation. The model is fit to trained model and predicted for test model.

### Metrics

* Firstly, the model is worked with Prophet's inbuilt cross-validation at some cut-off points. This cross-validation measure forecast error from historical data.
* The cross-validation evaluates metrics such as Mean-squared error(MSE), Root Mean squared error(RMSE), Mean Averaged Error(MAE), MAPE(Mean Averaged Percentage Error) and few more.
* In my model, the MSE and MAPE is evaluated through raw code for both training and testing data. This is done because we get the overall metrics of all dates and not at particular cut-off points.
* Finally, the model is predicted with sales value for 3 month period and saved in a csv file.

### Stay tuned

* The model will be deloyed via streamlit and heroku for better understanding with visualization and the link will be updated in this README file.



