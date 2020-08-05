import os
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

def getData():
    # Get home data from CSV file
    dataFile = None
    if os.path.exists('alonhadat.csv'):
        
        dataFile = pd.read_csv('alonhadat.csv')

    return dataFile

def linearRegressionModel(X_train, Y_train, X_test, Y_test):
    linear = linear_model.LinearRegression()
    # Training process
    linear.fit(X_train, Y_train)
    # Evaluating the model
    score_trained = linear.score(X_test, Y_test)
    #Xtest = [[7,50,8]]
    #print(Xtest)
    #Ypred = linear.predict(Xtest)
    #print(Ypred)
    return score_trained

def lassoRegressionModel(X_train, Y_train, X_test, Y_test):
    lasso_linear = linear_model.Lasso(alpha=0.1)
    # Training process
    lasso_linear.fit(X_train, Y_train)
    # Evaluating the model
    score_trained = lasso_linear.score(X_test, Y_test)

    return score_trained


from sklearn.model_selection import GridSearchCV
def model_gradient_boosting_tree(X_train,X_test,Y_train):
    gbr = ensemble.GradientBoostingRegressor()
    param_grid = {
        'n_estimators': [100],
        'max_features': [7],
        'max_depth': [6,15],
        'learning_rate': [0.01,0.02,0.05],        
    }
    model = GridSearchCV(estimator=gbr, param_grid=param_grid, n_jobs=4, cv=10, scoring='r2')
    model.fit(X_train, Y_train)
    print('Gradient boosted tree regression...')
    print('Best Params:')
    print(model.best_params_)
    #print('Best CV Score:')
    #print(-model.best_score_)

    y_pred = model.predict(X_test)
    return y_pred, -model.best_score_


from sklearn import ensemble
def GBD(X_train,Y_train,X_test,Y_test):
    clf = ensemble.GradientBoostingRegressor(n_estimators = 100, max_depth = 6, learning_rate = 0.05,loss='ls')
    clf.fit(X_train, Y_train)
    score = clf.score(X_test,Y_test)
    score = score
    return score 


if __name__ == "__main__":
    data = getData()
    if data is not None:
        # Selection few attributes
       

        data = data[np.abs(data["price"]-data["price"].mean())<=(2*data["price"].std())]
        data = data[np.abs(data["road-width"]-data["road-width"].mean())<=(3*data["road-width"].std())]
        data = data[np.abs(data["bedroom_no"]-data["bedroom_no"].mean())<=(3*data["bedroom_no"].std())]
        data = data[np.abs(data["square_meter"]-data["square_meter"].mean())<=(3*data["square_meter"].std())]
        data = data[np.abs(data["floors"]-data["floors"].mean())<=(3*data["floors"].std())]


        # Vector price of house

        attributes = list(
            [   
                #'month_2020',
                'street',
                'area',
                'district',
                'floors',
                'bedroom_no',
                'square_meter',
                'road-width'                
            ]
        )
        

        Y = data['price']
        #print(data['price'].describe())
        #print(data['road-width'].describe())
        #print(data['bedroom_no'].describe())
        #print(data['floors'].describe())
        #print(data['square_meter'].describe())

        train_corr = data.select_dtypes(include=(np.number))
        corr = train_corr.corr()
        plt.subplots(figsize=(20,9))
        sns.heatmap(corr, annot=True)
        plt.show()

        #plt.scatter(data['price'],data['bedroom_no'])
        #plt.xlabel('Bedroom')
        #plt.ylabel('Price')
        #plt.show()
        #plt.scatter(data['price'],data['road-width'])
        #plt.xlabel('Road')
        #plt.ylabel('Price')
        #plt.show()

        # print np.array(Y)
        # Vector attributes of house
        X = data[attributes]

        
        # Split data to training test and testing test
        X_train, X_test, Y_train, Y_test = train_test_split(np.array(X), np.array(Y), test_size=0.2)
        # Linear Regression Model
        #apply SelectKBest class to extract top 10 best features
        



        linearScore = linearRegressionModel(X_train, Y_train, X_test, Y_test)
        print('Linear Score = ' , linearScore)
        # LASSO Regression Model
        lassoScore = lassoRegressionModel(X_train, Y_train, X_test, Y_test)
        print('Lasso Score = ', lassoScore)

        GDBc = GBD(X_train, Y_train, X_test, Y_test)
        print('GBR =', GDBc)

        c = model_gradient_boosting_tree(X_train,X_test,Y_train)
        print(c)

        

        