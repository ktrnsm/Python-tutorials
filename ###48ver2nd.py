import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
import sklearn.metrics as mt

original_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.csv")
data = original_data.copy()

y = data["Sales"]
X = data.drop(columns="Sales", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

def model_prediction(model, degree=1):
    # Generate polynomial features
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    # Train and predict using the polynomial features
    model.fit(X_train_poly, y_train)
    prediction = model.predict(X_test_poly)
    
    # Calculate performance metrics
    r2 = mt.r2_score(y_test, prediction)
    rmse = mt.mean_squared_error(y_test, prediction, squared=False)
    return [r2, rmse]

models = [LinearRegression(), Ridge(), Lasso(), ElasticNet(), SVR(), DecisionTreeRegressor(random_state=0), BaggingRegressor(random_state=0), RandomForestRegressor(random_state=0)]
degrees = [1, 2, 3] # Test polynomial degrees 1, 2, and 3
name = ["Linear", "Ridge", "Lasso", "ElasticNet", "SVR", "DecisionTree", "Bagging", "RandomForest"]
result = []
for d in degrees:
    for i in models:
        result.append(model_prediction(i, degree=d))
df = pd.DataFrame(name * len(degrees), columns=["Model Name"])
df["Degree"] = degrees * len(models)
df2nd = pd.DataFrame(result, columns=["R2", "RMSE"])
df = df.join(df2nd)
print(df)
